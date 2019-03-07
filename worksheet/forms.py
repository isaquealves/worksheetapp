from django.contrib.auth.models import User
from django import forms
from .models import TransactionType, Transaction

class TransactionForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    kind = forms.ChoiceField(
        choices=TransactionType.choices(),
        widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    amount = forms.DecimalField(
        max_digits=19,
        decimal_places=4,
        widget=forms.TextInput({
            'class': 'form-control'
        }))
    class Meta:
        model = Transaction
        exclude = ('user',)

