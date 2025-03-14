from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Receipt, ExpenseCategory, Account
from .forms import ReceiptForm

@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {'receipts': receipts}
    return render(request, 'receipts/receipts_list.html', context)

@login_required
def create_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect('home')
    else:
        form = ReceiptForm()

    return render(request, 'receipts/create_receipt.html', {'form': form})

@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {'categories': categories}

    return render(request, 'receipts/category_list.html', context)

@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    return render(request, 'receipts/account_list.html', {'accounts': accounts})
