from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Receipt

@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {'receipts': receipts}
    return render(request, 'receipts/receipt_list.html', context)

def show_receipt(request):
    receipts = Receipt.objects.all()
    context = {
        "show_receipt": receipts,
    }
    return render(request, "receipts/list.html", context)

class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = 'receipt_list.html'

    def get_queryset(self):
        # Filter receipts by the logged-in user
        return Receipt.objects.filter(purchaser=self.request.user)
