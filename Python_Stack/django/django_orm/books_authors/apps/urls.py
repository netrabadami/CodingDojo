from django.urls import path
from . import views

urlpatterns  =[
    path('',views.home),
    path('create',views.create),
    path('book/<int:id>',views.view),
    path('authors',views.authors),
    path('createAuthor',views.createAuthor),
    path('addAuthor/<int:id>',views.addAuthor),
    path('author/<int:id>',views.viewAuthor),
    path('addBook/<int:id>',views.addBook)

]