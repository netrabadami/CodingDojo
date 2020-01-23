from django.urls import path
from . import views

urlpatterns = [
    path('shows/new',views.new_show),
    path('create',views.create),
    path('show/<int:id>',views.view_show)
]