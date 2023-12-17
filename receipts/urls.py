from django.urls import path
from . import views
from .views import receipt_list, ReceiptListView

urlpatterns = [
    path('', views.receipt_list, name='home'),
    path('receipts/', receipt_list, name='receipt_list'),
    path('receipts/', ReceiptListView.as_view(), name='receipt-list'),

]
