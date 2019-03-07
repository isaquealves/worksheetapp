from django.urls import path

from worksheet import views

urlpatterns = ***REMOVED***
    path('', views.transaction_list, name='transaction_index'),
    path('form/', views.create_transaction, name='transaction_form')
***REMOVED***