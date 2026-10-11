from django.urls import path
from . import views

urlpatterns = [
    # The display page
    path('', views.blog_post_display, name="blog_post_display"),

    # Change the name here to "Blog_Post_Delete" so it matches your HTML template
    path('delete/<int:id>/', views.delete_post, name="Blog_Post_Delete"),
]