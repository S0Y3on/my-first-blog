from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Post

from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import PostSearchForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect
from django.http import HttpResponse
from lxml import etree
import requests

# Create your views here.


@csrf_exempt
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@csrf_exempt
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            # if request.POST.get('upload_file', True):
            #     post.upload_file = request.FILES['upload_file']
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})


@csrf_exempt
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            # if request.POST.get('upload_file', True):
            #     post.upload_file = request.FILES['upload_file']
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})


@csrf_exempt
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


@csrf_exempt
def post_search(request):
    form = PostSearchForm(request.GET)
    context = {}
    context['form'] = form

    if form.is_valid():
        searchWord = form.cleaned_data['search_word']
        posts = Post.objects.filter(Q(title__contains=searchWord) | Q(text__contains=searchWord)).distinct()
        context['search_term'] = searchWord
        context['object_list'] = posts

    return render(request, 'blog/post_search.html', context)

    # return render(request, 'blog/post_list.html', {'posts': posts})
    # return render(request, 'blog/post_search.html', {'posts': posts})


@csrf_exempt
def post_test(request):
    return render(request, 'blog/post_test.html')


@csrf_exempt
def index(request):
    return render(request, 'blog/xxe_test.html')


@csrf_exempt
def result(request):
    name = request.POST["data"]
    try:
        parser = etree.XMLParser(load_dtd=True,  no_network=False,  resolve_entities=True)
        name = etree.fromstring(name, parser)
    except etree.XMLSyntaxError as e:
        print("[ Error Log ] : %s \n\n"%e )
        return None
    name = name.text
    return render(request, 'blog/result.html', {'name': name} )