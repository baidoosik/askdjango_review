from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Article,Comment
from .forms import *
from django.contrib import messages
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


def post_detail(request,id):
    post = get_object_or_404(Post,id=id)

    comments = post.comment_set.all()

    return render(request,'blog/post_detail.html',{
        'post':post,
        'comments':comments,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST,request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.author =request.user
            post = form.save()
            messages.success(request, '성공적으로 POST 하였습니다 !')

            return redirect('blog:post_list')
    else:
        form = PostModelForm()

    return render(request,'blog/post_new.html',{
        'form':form
    })


