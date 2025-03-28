from django.urls import path
from . import views
from .views import receipt_list, create_receipt, category_list, account_list

urlpatterns = [
    path('', receipt_list, name='receipt_list'),
    path('create/', create_receipt, name='create_receipt'),
    path('categories/', category_list, name='category_list'),
    path('accounts/', account_list, name='account_list'),

]
