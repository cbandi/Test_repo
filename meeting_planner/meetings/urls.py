from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.details, name='detail'),
    path('room', views.room, name='rooms'),
    path('new', views.new, name='new')
]
