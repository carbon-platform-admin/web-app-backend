from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from ..serializers import BlogSerializer

from ..models import Blog

@api_view(['GET'])
def get_blog_by_title(request, blog_title, *args, **kwargs):
    try:
        blog = Blog.objects.get(title=blog_title)
    except:
        return Response({'detail': 'error fetching blog'})
    
    serializer = BlogSerializer(blog)
    
    return Response(serializer.data, 200)

@api_view(['GET'])
def get_recent_blogs(request, *args, **kwargs):
    blogs = []
    try: 
        blogs = Blog.objects.filter(blog_type="B").order_by("-timestamp")
    except:
        blogs = []
    
    blog_serial = BlogSerializer(blogs, many=True)
    
    return Response(blog_serial.data[:3], status=200)


@api_view(['GET'])
def get_vlogs(request, *args, **kwargs):
    try: 
        vlogs = Blog.objects.filter(blog_type="V").order_by("-timestamp")
    except:
        vlogs = []
    
    vlog_serial = BlogSerializer(vlogs, many=True)
    
    return Response(vlog_serial.data[:10], status=200)

@api_view(['GET'])
def get_articles(request, *args, **kwargs):
    articleDict = {}
    
    try:
        articles = Blog.objects.filter(blog_type="A").all()
    except:
        return Response({'detail': 'Error fetching articles'}, status=500)
    
            
    serializer = BlogSerializer(articles, many=True)
    
    
    for article in serializer.data:
        article = json.loads(json.dumps(article))
        existing = articleDict.setdefault(article['category'], [article])
        
        if article not in existing:
            existing.append(article)
            articleDict[article["category"]] = existing
            
    return Response(articleDict, 200)


@api_view(['GET'])
def get_recent_articles(request, *args, **kwargs):
    recent = []
    
    try:
        recent = Blog.objects.filter(blog_type="A").order_by('-timestamp').all()[:10]
    except:
        return Response({"detail": "error fetching recent articles"}, 500)

    serializer = BlogSerializer(recent, many=True)
    
    return Response(serializer.data, 200)
    
            