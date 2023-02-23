from django.urls import path

from .views import (
    get_recent_blogs,
    get_vlogs,
    get_articles,
    get_recent_articles,
    get_blog_by_title
)

urlpatterns = [
    path('recent', get_recent_blogs),
    path('vlogs', get_vlogs),
    path('articles', get_articles),
    path('articles/recent', get_recent_articles),
    path('<str:blog_title>', get_blog_by_title)
]