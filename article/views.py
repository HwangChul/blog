from django.shortcuts import render
from .models import ArticlePost
# Create your views here.
def article_list(request):
    #从blogPost取出所有文章
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)
