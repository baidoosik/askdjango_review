from django.shortcuts import render,HttpResponse

# Create your views here.

# default 적용, 하나의 함수에 여러 url 연결.
def add_view(request,x,y=0,z=0):
    result = int(x)+int(y) +int(z)
    return HttpResponse(result)