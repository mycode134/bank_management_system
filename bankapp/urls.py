from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_cus, name='add_cus'),
    path('edit/<int:cus_id>/', views.edit_cus, name='edit_cus'),
    path('delete/<int:cus_id>/', views.delete_cus, name='delete_cus'),
    path('', views.view_all_cus, name='view_all_cus'),
    path('filter/', views.filter_cus, name='filter_cus'),
    path('transfer_money/', views.transfer_money, name='transfer_money'),
]