from django.shortcuts import render, HttpResponse

from . import models


# Create your views here.

def article_list(request):
    articles = models.article.objects.all().order_by('-date')
    args = {'articles': articles}
    return render(request, 'myblog/myblog.html', args)


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.article.objects.get(slug=slug)
    return render(request, 'myblog/article_detail.html', {'article': article})
