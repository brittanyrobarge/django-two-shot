from django.contrib import admin
from .models import ExpenseCategory, Receipt, Account
# Register your models here.
admin.site.register(ExpenseCategory)
admin.site.register(Receipt)
admin.site.register(Account)
