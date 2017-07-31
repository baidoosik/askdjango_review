from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Article,Comment
from .forms import PostModelForm,CommentModelForm
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
    post = Post.objects.prefetch_related('comment_set').filter(id=id).first()

    if request.method == "POST":
        form = CommentModelForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author =request.user
            comment.save()
            return redirect(post)
    else:
        form = CommentModelForm()
    return render(request,'blog/post_detail.html',{
        'post':post,
        'form':form
    })


def post_new(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST,request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.author =request.user
            post = form.save()
            messages.add_message(request, messages.INFO, '포스팅이 완료됐습니다.')

            return redirect('blog:post_list')
    else:
        form = PostModelForm()

    return render(request,'blog/post_new.html',{
        'form':form
    })

def post_edit(request,id):
    post = get_object_or_404(Post,id=id)

    if request.method =='POST':
        form = PostModelForm(request.POST,request.FILES,instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.add_message(request, messages.INFO, '글 수정이 완료됐습니다.')

            return redirect('blog:post_list')
    else:
        form =PostModelForm(instance=post)

    return render(request,'blog/post_new.html',{
        'form':form
    })


