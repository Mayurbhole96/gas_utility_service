from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.filter(is_deleted = False,is_active = True).order_by('-id')
    serializer_class = ServiceRequestSerializer

    def list(self, request):
        if 'customer' in self.request.GET:
            temp_obj = ServiceRequest.objects.filter(customer=request.GET["customer"],is_deleted__in = [False])
            serializer = ServiceRequestSerializer(temp_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)
        else:
            temp_obj = ServiceRequest.objects.filter(is_deleted = False,is_active = True).order_by('-id')
            serializer = ServiceRequestSerializer(temp_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ServiceRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Record Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)       
    
    def update(self, request, pk=None, partial=True):  
        temp_obj = ServiceRequest.objects.get(id=pk)
        serializer = ServiceRequestSerializer(temp_obj,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Record Updated Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self):
        return Response({"status":"Record Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
    
class RequestTrackingViewSet(viewsets.ModelViewSet):
    queryset = RequestTracking.objects.all()
    serializer_class = RequestTrackingSerializer

    def list(self, request):
        temp_obj = RequestTracking.objects.all()
        serializer = RequestTrackingSerializer(temp_obj, many=True)
        if serializer.data:
            return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)    

    # def create(self, request):
    #     serializer = RequestTrackingSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status":"Record Added Successfully"},status=status.HTTP_201_CREATED)
    #     else:
    #         return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    def update(self, request, pk=None, partial=True):  
        temp_obj = RequestTracking.objects.get(id=pk)
        serializer = RequestTrackingSerializer(temp_obj,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Record Updated Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
 