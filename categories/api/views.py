from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Category
from ..serializers import CategorySerializer

@api_view(['GET'])
def get_root_categories(request, *args, **kwargs):
    # We try to get the categories with no parent
    try:
        roots = Category.objects.filter(parent=None).all()
    except:
        return Response({"detail", "No root categories found"}, status=400)

    serializer = CategorySerializer(roots, many=True)
    return Response({'content': sorted(serializer.data, key=lambda i: (i['name'])), 'content_length': len(serializer.data)})


@api_view(['GET'])
def get_featured_categories(request, *args, **kwargs):
    
    featured = Category.objects.filter(featured=True).all()
    
    serializer = CategorySerializer(featured, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_all_categories(request, *args, **kwargs):
    categories = Category.objects.all()
    
    serializer = CategorySerializer(categories, many=True)
    
    return Response(serializer.data, 200)


    