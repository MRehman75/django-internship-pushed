from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('posts/<int:post_id>/', views.posts, name='posts'),

    # Bonus
    path('posts/<int:post_id>/<slug:slug>/', views.post_slug, name='post_slug'),
]