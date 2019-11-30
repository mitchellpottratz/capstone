from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from users.models import User
from .models import Company


# this view is where registered company users can join 
# a company by using the companies invite code
def join(request):
	return HttpResponse('join company page')



