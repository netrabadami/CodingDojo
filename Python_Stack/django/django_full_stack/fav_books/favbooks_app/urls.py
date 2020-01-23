from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('registration/process',views.reg_process),
    path('login/process',views.login_process),
]