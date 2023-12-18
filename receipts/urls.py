from django.urls import path
from . import views
from .views import receipt_list, create_receipt

urlpatterns = [
    path('', receipt_list, name='receipt_list'),
    path('receipts/create/', create_receipt, name='create_receipt'),

]
