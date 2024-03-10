from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("user_list",views.user_list),
    path("user_add",views.user_add),
]