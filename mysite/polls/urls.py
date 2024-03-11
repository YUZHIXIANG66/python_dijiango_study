from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("user_list",views.user_list),
    path("user_add",views.user_add),
    path("model_test",views.model_test),
    path("news",views.news),
    path("user_register",views.user_register),
    path("register",views.post_register),
    path('user_login',views.user_login),
    path("login",views.post_login)
]