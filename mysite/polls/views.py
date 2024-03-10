from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello,world.You're at the polls index.")

def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")
