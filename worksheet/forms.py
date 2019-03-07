from django.contrib.auth.models import User
from django import forms
from .models import TransactionType, Transaction

class TransactionForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs=***REMOVED***
        'class': 'form-control'
***REMOVED***))
    kind = forms.ChoiceField(
        choices=TransactionType.choices(),
        widget=forms.Select(attrs=***REMOVED***
        'class': 'form-control'
***REMOVED***))
    amount = forms.DecimalField(
        max_digits=19,
        decimal_places=4,
        widget=forms.TextInput(***REMOVED***
            'class': 'form-control'
    ***REMOVED***))
    class Meta:
        model = Transaction
        exclude = ('user',)

