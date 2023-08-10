from rest_framework import serializers
from .models import *

class ServiceRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceRequest
        fields = '__all__'

    def create(self, validated_data):   
        service_request_id =  ServiceRequest.objects.create(**validated_data)
        RequestTracking.objects.create(service_request = service_request_id)
        return service_request_id
    
    def update(self, instance, validated_data):   
        instance.resolved = validated_data.get('resolved', instance.resolved)
        instance.resolution_date = validated_data.get('resolution_date', instance.resolution_date)
        instance.save()
        RequestTracking.objects.filter(service_request = instance.id).update(status = "Resolved")

        return instance
    

class RequestTrackingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestTracking
        fields = '__all__'    