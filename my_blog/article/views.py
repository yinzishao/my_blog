from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    posts = Article.objects.all()
    paginator =  Paginator(posts,3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request,'home.html',{"post_list":contacts})
    # return render(request,'test.html')
    # return HttpResponse(str(2))

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'archives.html',{'post_list':post_list})

def search_tag(request, tag) :
        try:
            post_list = Article.objects.filter(category__iexact = tag) #contains
        except Article.DoesNotExist :
            raise Http404
        return render(request, 'tag.html', {'post_list' : post_list})
