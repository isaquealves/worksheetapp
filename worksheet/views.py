from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from worksheet.models import Transaction

from .forms import TransactionForm

@login_required
def transaction_list(request):
    context = ***REMOVED******REMOVED***
    if request.user:
        transactions = Transaction.objects.all()
        context***REMOVED***'transactions'***REMOVED*** = transactions

    return render(request, 'transactions/index.html', context)

@login_required
def create_transaction(request, form=None):

    if request.method == 'POST':
        data = request.POST
        form = TransactionForm(data=data)
        import pudb; pudb.set_trace()
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return HttpResponseRedirect(reverse('transaction_index'))

    form = TransactionForm()
    view_context = ***REMOVED***
        'request': request,
        'form':form
***REMOVED***
    return render(request,
                  'transactions/transaction.html',
                  context=view_context)

def auth(request):
    if request.method == 'POST':
        username = request.POST***REMOVED***'username'***REMOVED***
        password = request.POST***REMOVED***'password'***REMOVED***
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('transaction_index'))
    return render(request, 'auth/login.html')



def app_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('transaction_index'))


