from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import TagSerializer

from ..models import Tag

@api_view(['GET'])
def get_all_tags(request, *args, **kwargs):
    tags = []
    try: 
        tags = Tag.objects.all()
    except:
        return Response({'detail': 'Error getting tags'}, status=500)
    
    tag_serial = TagSerializer(tags, many=True)
    
    return Response(tag_serial.data, status=200)