from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chickens/', views.ChickensIndex.as_view(), name='index'),
    path('chickens/<int:pk>/', views.ChickensDetail.as_view(), name='detail'),
    path('chickens/create/', views.ChickensCreate.as_view(), name='chickens_create'),
    path('chickens/<int:pk>/update', views.ChickenUpdate.as_view(), name='chickens_update'),
    path('chickens/<int:pk>/delete', views.ChickenDelete.as_view(), name='chickens_delete'),
]
