from django.urls import path

from worksheet import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_index'),
    path('form/', views.create_transaction, name='transaction_form'),
    path('login', views.auth, name='worksheet_login'),
    path('logout', views.app_logout)
]