from django.shortcuts import render
from .models import Post,Article
# Create your views here.
def post_list(request):
    query = Post.objects.all()

    q = request.GET.get('q','')

    if q:
        query=query.filter(title__icontains=q)

    return render(request,'blog/post_list.html',{
        'post':query
    })
