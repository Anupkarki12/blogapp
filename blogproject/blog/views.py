from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from .models import Post, Comment

# List all published posts
def post_list(request):
    posts = Post.published.all()  # Using custom manager from Post model
    return render(request, 'blog/post_list.html', {'posts': posts})

# Post detail page
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

# Create new post
@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status', 'draft')
        image = request.FILES.get('image')
        
        post = Post.objects.create(
            author=request.user,
            title=title,
            content=content,
            status=status,
            image=image
        )
        return redirect('post_detail', slug=post.slug)
    
    return render(request, 'blog/create_post.html')

# Add comment to post
@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        
        Comment.objects.create(
            post=post,
            user=request.user,
            content=content
        )
        return redirect('post_detail', slug=slug)
    
    return redirect('post_detail', slug=slug)


# User registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
