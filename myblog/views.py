from django.shortcuts import render
from . import models


# Create your views here.

def article_list(request):
    articles = models.article.objects.all().order_by('date')
    args = {'articles':articles}
    return render(request, 'myblog/myblog.html' , args)


