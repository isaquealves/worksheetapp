from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from worksheet.models import Transaction

from .forms import TransactionForm


def transaction_list(request):
    context = ***REMOVED******REMOVED***
    if request.user:
        transactions = Transaction.objects.all()
        context***REMOVED***'transactions'***REMOVED*** = transactions

    return render(request, 'transactions/index.html', context)


def create_transaction(request, form=None):

    if request.method == 'POST':
        data = request.POST
        form = TransactionForm(data=data)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return HttpResponseRedirect('index_view')

    form = TransactionForm()
    view_context = ***REMOVED***
        'request': request,
        'form':form
***REMOVED***
    return render(request,
                  'transactions/transaction.html',
                  context=view_context)

def login(request):
    username = request.POST***REMOVED***'username'***REMOVED***
    password = request.POST***REMOVED***'password'***REMOVED***
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(redirect_to='transaction_index')
def logout(request):
    logout(request)


