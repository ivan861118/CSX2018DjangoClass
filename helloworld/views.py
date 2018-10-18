from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from myapp.models import TextMessage



def index(request):
    if 'user_name' and 'user_msg' in request.GET:
        new_msg = TextMessage.objects.create(talker = request.GET['user_name'], message = request.GET['user_msg'])
    msgs = TextMessage.objects.all()
    return render(request, 'index.html',locals())


	

