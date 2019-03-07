from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from v1.api import views


urlpatterns = [
    path('transactions/', views.TransactionView.as_view(), name='transaction_list'),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transaction_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)