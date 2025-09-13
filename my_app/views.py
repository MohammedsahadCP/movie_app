from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render 

# Create your views here.
def any(request):
       movie_details={
              'title':'Lokha',
              'year':'2025',
              'summary':'story of neeli'
       }
       return render(request,'hello.html',movie_details)
