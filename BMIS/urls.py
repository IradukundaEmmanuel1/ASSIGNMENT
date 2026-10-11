from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', views.home),
    path('', views.home), # Root URLs

    # Learning Dynamic URLs
    path('course/<int:course_id>', views.course),
    path('courseName/<str:course_name>', views.courseName),
    path('courseBlog/<slug:course_blog_title>', views.courseBlog),
    path("studentMarks/", views.studentMarks),

    # Change 'blog.urls' to 'Blog.urls' to match your folder name exactly
    path('blog/', include('Blog.urls')),
]