from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
<<<<<<< HEAD
	return render(request, 'guestbookver1.html')
=======
	return HttpResponse('Hello World,I am Ivan' )
>>>>>>> 48dee432b92e2e7e381d2a6c864dd8a7c54d2806
