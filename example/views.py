from django.shortcuts import render,HttpResponse
from django.views.generic import View

# Create your views here.

# default 적용, 하나의 함수에 여러 url 연결.
def add_view(request,x,y=0,z=0):
    result = int(x)+int(y) +int(z)
    return HttpResponse(result)


def name_view(request,name):
    return HttpResponse('''
              <h1> Askajngo Review </h1>
              <h2> {name}</h2>
              <p> 하루만에 장고 기본편 복습하기!!!파이어~ </p>'''.format(name=name))


def name_anotherview(request,name2):
    return render(request,'example/layout.html',{
        'name':name2
    })

class SampleTemplateView(View):
    @classmethod
    def as_view(cls,template_name):
        def view_fn(request):
            return render(request, template_name)
        return view_fn

fbv_view = SampleTemplateView.as_view('example/post_list.html')