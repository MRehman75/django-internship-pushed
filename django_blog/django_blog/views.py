from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    posts = Post.objects.filter(published=True)

    return render(request, "home.html", {
        "posts": posts
    })


def about(request):
    return HttpResponse("<h1>About Us</h1><p>This page contains information about the blog.</p>")


def contact(request):
    return HttpResponse("<h1>Contact</h1><p>Email: contact@example.com</p>")


def posts(request, post_id):
    return HttpResponse(f"<h1>Posts</h1><p>You requested post number {post_id}.</p>")


def post_slug(request, post_id, slug):
    return HttpResponse(f"<h1>Post Details</h1><p>ID: {post_id}</p><p>Slug: {slug}</p>")