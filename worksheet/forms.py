from django.contrib.auth.models import User
from django import forms
from .models import TransactionType, Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        
