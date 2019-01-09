from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ExpenseManager(models.Manager):
    def get_queryset(self):
        return super(ExpenseManager, self).get_queryset().filter(operayion_type='expense')

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    OPERATION_CHOICES = (
        ('expense', 'Expense'),
        ('revenue', 'Revenue'),
    )
    categorie = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='transactions')
    operation_type = models.CharField(max_length=10, choices=OPERATION_CHOICES, default='expense')
    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.description

    objects = models.Manager()
    expenses = ExpenseManager()
