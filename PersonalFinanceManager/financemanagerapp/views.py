from django.shortcuts import render, get_object_or_404
from .models import Category, Transaction
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/list.html', { 'categories': categories })

def category_detail(request, name):
    category = get_object_or_404(Category, name=name)
    return render(request, 'categories/detail.html', { 'category': category })

@login_required
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/list.html', { 'transactions': transactions })
