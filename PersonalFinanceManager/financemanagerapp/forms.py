from django import forms
from django.contrib.auth.models import User
from .models import Category, Transaction

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class TransactionForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['categorie'].widget = forms.Select(choices=((x.id, x.name) for x in Category.objects.filter(user=user)))
        self.fields['date'].widget = DateInput()
    
    class Meta:
        model = Transaction
        fields = ['categorie', 'operation_type', 'value', 'date', 'description']
    