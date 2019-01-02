from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('categories/', views.category_list, name='categories_list'),
    path('transactions/', views.transaction_list, name='transactions_list'),    
]