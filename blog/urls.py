from django.urls import path
from .views import BlogListView, PostDetailView

app_name="blog"

urlpatterns = [

    path('post/', BlogListView.as_view()),
    path('post/<post_slug>/', PostDetailView.as_view()),

    
]