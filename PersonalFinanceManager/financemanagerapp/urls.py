from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    path('categories/', views.category_list, name='categories_list'),
    path('transactions/', views.transaction_list, name='transactions_list'),
    #path('login/', views.user_login, name='login')
]