from django.shortcuts import render
from .models import Articles,Category,Tag

# FBV   functions based view 基于函数


def index(request):
    articles = Articles.objects.all()
    lastest_articles=articles[:5]
    categories=Category.objects.all()
    tags=Tag.objects.all()
    context={
        "articles":articles,
        "lastest_articles":lastest_articles,
        "categories":categories,
        "tags":tags
    }
    return render(request,'index.html',context)


def detail(request,pk):
    article = Articles.objects.get(pk=pk)
    article.increace_visited()
    lastest_articles=Articles.objects.all()[:5]
    categories=Category.objects.all()
    tags=Tag.objects.all()
    context={
        'article':article
    }
    return render(request,'single_article.html',context)


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')  

