from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


# Create your views here.

def article_list(request):
    articles = models.article.objects.all().order_by('-date')
    args = {'articles': articles}
    return render(request, 'myblog/myblog.html', args)


@login_required(login_url='/accounts/login')
def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.article.objects.get(slug=slug)
    return render(request, 'myblog/article_detail.html', {'article': article})


def create_article(request):
    if request.method == 'post':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('myblog:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'myblog/create_article.html', {'form': form})
