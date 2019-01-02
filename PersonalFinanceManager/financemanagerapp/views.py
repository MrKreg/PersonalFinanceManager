from django.shortcuts import render, get_object_or_404
from .models import Category, Transaction

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/list.html', { 'categories': categories })

def category_detail(request, name):
    category = get_object_or_404(Category, name=name)
    return render(request, 'categories/detail.html', { 'category': category })

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/list.html', { 'transactions': transactions })
