from django.shortcuts import render
import requests

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello,world.You're at the polls index.")

def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")

def model_test(request):
    name = "Zhao"
    roles = ["管理","CEO","保安"]
    user_info={"name":"YU","salary":1000,'role' : 'CEO'}
    return render(request,"model_test.html",{"n1":name,"n2":roles,"user_info":user_info})

def news(request):
    #发请求：https://ldocctvwbcdali.v.myalicdn.com/ldocctvwbcd/cdrmldcctv4_1md.m3u8
    res = requests.get("https://ldocctvwbcdali.v.myalicdn.com/ldocctvwbcd/cdrmldcctv4_1md")
    print(res)
    return render(request,'news.html')

# 用户注册
def user_register(request):
    return render(request,"user_register.html")

def post_register(request):
    res=request.POST
    print('-------------------------------------------------------')
    print(res)
    print(f"name : {res['username']}    psw : {res['password']}     gender : {res['gender']}")
    print('-------------------------------------------------------')
    return HttpResponse(f"{res['username']}     {res['password']}   {res['gender']}")

#用户登录
def user_login(request):
    return  render(request,"user_login.html")

def post_login(request):
    res=request.POST
    print('-------------------------------------------------------')
    print(res)
    print(f"name : {res['username']}    psw : {res['password']}")
    print('-------------------------------------------------------')
    return HttpResponse(f"{res['username']}     {res['password']}")

if __name__== '__main__':
    res = requests.get("https://ldocctvwbcdali.v.myalicdn.com/ldocctvwbcd/cdrmldcctv4_1md")
    print(res)

