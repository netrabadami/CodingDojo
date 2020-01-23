from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('shows/new',views.new_show),
    path('create',views.create),
    path('show/<int:id>',views.view_show),
    path('shows',views.view_all_shows),
    path('show/<int:id>/edit',views.edit_show),
    path('edit/<int:id>',views.edit),
    path('show/<int:id>/delete',views.delete)

]