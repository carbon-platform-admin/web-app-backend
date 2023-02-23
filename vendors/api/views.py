from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from urllib.parse import unquote

from ..models import Vendor
from ..serializers import VendorSerializer

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET'])
def get_featured_vendors(request, *args, **kwargs):
    try:
        vendor = Vendor.objects.all()
    except:
        return Response({"detail": "Vendors not found"}, status=500)
    
    serializer = VendorSerializer(vendor, many=True)
    
    return Response(serializer.data, status=200)

@api_view(['GET'])
def get_vendor_by_id(request, id, *args, **kwargs):
    try:
        vendor = Vendor.objects.get(id=id)
    except:
        return Response({"detail": "Vendor not found"})
    
    serializer = VendorSerializer(vendor)
    
    return Response({'content': serializer.data}, status=200)

@api_view(['POST'])
def create_vendor(request, *args, **kwargs):
    """
        Fields: 
            - name
            - logo
    """
    
    try:
        vendor = Vendor.objects.get(name=request.POST.get('name'))
    except:
        pass
    
    if vendor:
        return Response({'detail': "Vendor name already exists"}, status=400)
    
    # trying to create a vendor
    try:
        new_vendor = Vendor.objects.create(name=request.POST.get('name'), logo=request.POST.get('logo'))
    except:
        return Response({'detail': 'error creating new vendor'}, status=500)
    
    serializer = VendorSerializer(new_vendor)
    return Response({'content': serializer.data}, status=201)

@api_view(['DELETE'])
def delete_vendor(request, id, *args, **kwargs):
    try:
        vendor = Vendor.objects.get(id=id)
    except:
        return Response({'detail': 'vendor not found'}, status=400)
    
    try:
        vendor.delete()
    except:
        return Response({'detail': 'error deleting vendor from db'}, status=500)
    
    serializer = VendorSerializer(vendor)
    return Response({'content': serializer.data})
    
    

