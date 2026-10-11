from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def blog_post_display(request):
    # Fetch all posts from the database
    posts = Post.objects.all()

    # Added 'blog/' to match your folder structure exactly
    return render(request, 'blog/blog_post_display.html', {'posts': posts})


def delete_post(request, id):
    # Find the post by its ID (from the URL) or return a 404 error
    post = get_object_or_404(Post, id=id)

    # Delete it from the database
    post.delete()

    # Refresh the page by redirecting back to the display view
    return redirect('blog_post_display')