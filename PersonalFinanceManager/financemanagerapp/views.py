from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Transaction
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, TransactionForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView

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

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'categories/list.html', { 'categories': categories })

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)
    return render(request, 'transactions/list.html', { 'transactions': transactions, 'categories': categories })

@login_required
def category_delete(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('/categories')

class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', 'description')
    template_name = 'categories/category_form.html'
    success_url = '/categories/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreateView, self).form_valid(form)

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name', 'description')
    template_name = 'categories/category_form.html'
    success_url = '/categories/'

@login_required
def transaction_delete(request, id):
    transaction = Transaction.objects.get(pk=id)
    transaction.delete()
    return redirect('/transactions')


class TransactionCreateView(CreateView):
    model = Transaction
    fields = ('categorie', 'operation_type', 'value', 'date', 'description')
    template_name = 'transactions/transaction_form.html'
    success_url = '/transactions/'
    form_class = TransactionForm

    def get_form(self):
        return self.form_class(self.request.user, **self.get_form_kwargs())

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TransactionCreateView, self).form_valid(form)

class TransactionUpdateView(UpdateView):
    model = Transaction
    fields = ('categorie', 'operation_type', 'value', 'date', 'description')
    template_name = 'transactions/transaction_form.html'
    success_url = '/transactions/'
    form_class = TransactionForm

    def get_form(self):
        return self.form_class(self.request.user, **self.get_form_kwargs())