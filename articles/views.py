from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def article(request):
    # return HttpResponse("home")
    articles = Article.objects.all().order_by('date')
    return render(request,'article.html',{'articles':articles})

def article_detail(request,slug):
    return HttpResponse(slug)
    