from django.urls import path
from .views import blog_grid, blog_details, blog_post, blog_delete, blog_update, personal_blog, post_like

app_name = 'Blog_app'

urlpatterns = [

    path('blog_grid/', blog_grid, name='blog_grid'),
    path('blog_details/<int:pk>/', blog_details, name='blog_details'),
    path('blog_post/', blog_post, name='blog_post'),
    path('blog_details/blog_delete/<int:pk>/', blog_delete, name='blog_delete'),
    path('blog_details/blog_update/<int:pk>/', blog_update, name='blog_update'),
    path('personal_blog/', personal_blog, name='personal_blog'),
    path('like/<int:pk>/', post_like, name='post_like'),

]
