from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
# from django.urls.conf import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Login to Gas Utility"
admin.site.site_title = "Welcome to Gas Utility's Dashboard"
admin.site.index_title = "Welcome to this Gas Utility's Portal"

router = routers.DefaultRouter()
router.register(r'service', views.ServiceRequestViewSet)
router.register(r'tracking', views.RequestTrackingViewSet)


urlpatterns = [
    path('', include(router.urls)),    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)