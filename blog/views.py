from django.shortcuts import render
from .models import Post,Article
# Create your views here.
def post_list(request):
    query1 = Post.objects.all()

    query2 = Article.objects.all()

    q = request.GET.get('q','')

    if q:
        query1=query1.filter(title__icontains=q)

        query2=query2.filter(title__icontains=q)

    return render(request,'blog/post_list.html',{
        'post1':query1,
        'post2':query2,
    })
