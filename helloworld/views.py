from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User



def index(request):
	info_dict = {'Name':'Ivan Cheng','content':'第三週作業','msg':'哈囉'}
	return render(request, 'index.html',{'info_dict': info_dict})

	

