from django.shortcuts import render
from django.http import HttpResponse


    
# Create your views here.
def say_hello(request):
   return render(request, 'hello.html',{'name':'Tunde'})
    #pull data fromDB
    #Transform data and send email
    # return HttpResponse('Hello World')