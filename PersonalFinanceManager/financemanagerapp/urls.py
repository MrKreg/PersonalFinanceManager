from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    path('categories/', views.category_list, name='categories_list'),
    path('create_category/', views.CategoryCreateView.as_view(), name='create_category'),
    path('update_category/<pk>', views.CategoryUpdateView.as_view(), name='update_category'),
    path('delete_category/<id>', views.category_delete, name='delete_category'),
    path('transactions/', views.transaction_list, name='transactions_list'),
    path('create_transaction/', views.TransactionCreateView.as_view(), name='create_transaction'),
    path('update_transaction/<pk>', views.TransactionUpdateView.as_view(), name='update_transaction'),
    path('delete_transaction/<id>', views.transaction_delete, name='delete_transaction'),
]