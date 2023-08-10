from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)    # "Gas Leak"
    details = models.TextField()   # "Strong smell of gas in the kitchen."
    attached_files = models.FileField(upload_to='service_request_files/', blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)   # request date (created)
    resolved = models.BooleanField(default=False)   # is resolved or not
    resolution_date = models.DateTimeField(blank=True, null=True)  # (for last updated)
    
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")

    class Meta:
        db_table = "tbl_service_request"
        verbose_name_plural = "Service Request"

    def delete(self):
        self.is_deleted = True
        self.is_active = False
        self.save()

    def __str__(self):
        return f"{self.customer}: {self.request_type}"
    

class RequestTracking(models.Model):
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    RESOLVED = 'Resolved'
    CANCELED = 'Canceled'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (RESOLVED, 'Resolved'),
        (CANCELED, 'Canceled'),
    ]
    service_request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tbl_request_tracking"
        verbose_name_plural = "Request Tracking"

    def __str__(self):
        return f"{self.service_request}: {self.status}"    