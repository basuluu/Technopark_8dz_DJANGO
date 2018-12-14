from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm, RegistrationForm, EditProfileForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect

def search_form(request):
    posts = sorting(request, flag_search=True)
    return render(request, 'dairy/post_list.html', {'posts': posts})

def sorting(request, flag_search=False):
    posts = 0
    if request.method == "POST":
        if request.POST['sort'] == 'desc':
            posts = Post.objects.filter(vision=True).order_by('-created_date')
        elif request.POST['sort'] == 'asc':
            posts = Post.objects.filter(vision=True).order_by('created_date')
        elif request.POST['sort'] == 'popular':
            posts = Post.objects.filter(vision=True).order_by("-hit_count_generic__hits")
        else:
            posts = Post.objects.filter(vision=True).order_by("hit_count_generic__hits")
    if flag_search:
        if posts:
            posts = posts.filter(title__contains=request.GET['q'])
        else:
            posts = Post.objects.filter(title__contains=request.GET['q'])
    return posts

def post_list(request):
    if request.method == "POST":
        posts = sorting(request)
    else:
        posts = Post.objects.filter(vision=True).order_by('created_date')
    return render(request, 'dairy/post_list.html', {'posts': posts})

def post_detail(request, id, page):
    post = get_object_or_404(Post, id_post=id)
    hit_count = HitCount.objects.get_for_object(post)
    HitCountMixin.hit_count(request, hit_count)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.id_post = post
            comment.save()
            return redirect('post_detail', id=id, page=page)
    form = CommentForm()
    comments = Comment.objects.filter(id_post=id).order_by('created_date')
    p = Paginator(comments, 5)
    dict_param = {'post': post,
                  'form': form,
                  'pages': range(1, p.num_pages + 1)}
    if p.num_pages == 0:
        dict_param['comments'] = comments
    elif p.num_pages <= int(page):
        dict_param['comments'] = p.page(p.num_pages)
    else:
        dict_param['comments'] =  p.page(page)
    return render(request, 'dairy/post_detail.html', dict_param)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', id=post.id_post, page=1)
    else:
        form = PostForm()
    return render(request, 'dairy/post_edit.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Post, id_post=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', id=post.id_post, page=1)
    else:
        form = PostForm(instance=post)
    return render(request, 'dairy/post_edit.html', {'form': form})

def register(request):
    form = RegistrationForm()
    auth.logout(request)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    return render(request, 'dairy/register.html', {'form': form})

def profile(request):
    user = request.user
    if user.is_anonymous:
        return HttpResponseRedirect('/login/')
    posts = Post.objects.filter(author=user)
    return render(request, 'dairy/profile.html', {'user': user,
                                                  'posts': posts})

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/profile/')
    else:
        user = request.user
        if user.is_anonymous:
            return HttpResponseRedirect('/login/')
        form = EditProfileForm(instance=request.user)
        return render(request, 'dairy/edit_profile.html', {'form': form})
