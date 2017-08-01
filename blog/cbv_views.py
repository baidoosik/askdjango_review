from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Article,Comment
from .forms import PostModelForm,CommentModelForm
from django.contrib import messages
from django.views.generic import DetailView

# 1단계 - FBV 버전
'''
def article_detail(request,id):
    article = get_object_or_404(Article,id=id)

    return render(request,'blog/article_detail.html',{
        'article':article
    })
'''

# 2단계 - 함수를 통해 , 뷰 생성 버전
'''
def generate_view_fn(model):
    def view_fn(requset,id):
        instance = get_object_or_404(model,id=id)
        instance_name = model._meta.model_name
        template_name = '{}/{}_detail.html'.format(model._meta.app_label,instance_name)
        return render(requset,template_name,{
            instance_name:instance
        })
    return view_fn

article_detail = generate_view_fn(Article)
'''

'''
# 3단계 - cbv 형태로 컨셉만 구현한 버젼
class DetailView:

    def __init__(self,model):
        self.model = model

    def get_object(self,*args,**kwargs):
        return get_object_or_404(self.model,id=kwargs['id'])

    def get_template_name(self):
        return '{}/{}_detail.html'.format(self.model._meta.app_label,self.model._meta.model_name)

    def dispatch(self,request,*args,**kwargs):
        return render(request,self.get_template_name(),{
            self.model._meta.model_name: self.get_object(*args,**kwargs)
        })
    @classmethod
    def as_view(cls,model):
        def view(request,*args,**kwargs):
            self =cls(model)
            return self.dispatch(request,*args,**kwargs)
        return view

article_detail = DetailView.as_view(Article)
'''

# 4단계 - 장고기본제공 detailview cbv 쓰기

article_detail =DetailView.as_view(model=Article,pk_url_kwarg='id')