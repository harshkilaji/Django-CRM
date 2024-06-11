from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('records/<int:pk>/', views.records, name='records'),
    path('add_record', views.add_record, name='add_record'),
    path('delete_records/<int:pk>/', views.delete_record, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
]
