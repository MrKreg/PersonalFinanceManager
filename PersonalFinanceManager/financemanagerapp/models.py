from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Categorie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250)

    class Meta:
        ordering = ('name')

    def __str__(self):
        return self.name

class Transaction(models.Model):
    OPERATION_CHOICES = (
        ('expense', 'Expense'),
        ('revenue', 'Revenue'),
    )
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='transactions')
    operation_type = models.CharField(max_length=10, choices=OPERATION_CHOICES, default='expense')
    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=250)
