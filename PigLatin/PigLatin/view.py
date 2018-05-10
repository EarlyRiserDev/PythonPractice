from django.http import HttpResponse
from django.shortcuts import render

def getData(request):
	#return HttpResponse('hello world')
	return render(request,'Home.html')

def Translate(request):
	return(request,'Translate.html',{"input":input})