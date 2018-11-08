from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from myapp.models import TextMessage



def index(request):
    if 'ok' in request.POST:
        user_name = request.POST["user_name"]
        user_msg = request.POST["user_msg"]      
        new_msg = TextMessage.objects.create(talker = user_name, message = user_msg)
    msgs = TextMessage.objects.all()
    return render(request, 'index.html',locals())##未來把local改掉



	

