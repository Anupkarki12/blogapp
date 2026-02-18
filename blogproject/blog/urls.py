from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Include Django's built-in auth URLs (provides /accounts/login/, /accounts/logout/, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Auth URLs (custom overrides if needed - place AFTER include)
    # path('register/', views.register, name='register'),          # User registration
    # Login/Logout are now handled by Django's built-in URLs above
    
    # Blog URLs
    path('', views.post_list, name='post_list'),                 # Homepage: list posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Post detail
    path('create/', views.create_post, name='create_post'),     # Create new post
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),  # Add comment
    
    # User registration (custom URL outside accounts/)
    path('register/', views.register, name='register'),
]
