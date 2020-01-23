from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('registration/process',views.reg_process),
    path('login/process',views.login_process),
    path('books',views.books),
    path('logout/<int:id>',views.logout),
    path('books/add',views.addbook),
    path('books/newadd',views.newbook),
    path('books/<int:id>',views.showbook),
    path('users/<int:id>',views.userinfo),
    path('books/confirm_delete_review/<int.id>',views.deletereview)
    

]