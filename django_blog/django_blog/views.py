from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Blog</h1><p>This is the home page.</p>")

def about(request):
    return HttpResponse("<h1>About Us</h1><p>This page contains information about the blog.</p>")

def contact(request):
    return HttpResponse("<h1>Contact</h1><p>Email: contact@example.com</p>")

def posts(request, post_id):
    return HttpResponse(f"<h1>Posts</h1><p>You requested post number {post_id}.</p>")

# Bonus
def post_slug(request, post_id, slug):
    return HttpResponse(f"<h1>Post Details</h1><p>ID: {post_id}</p><p>Slug: {slug}</p>")
