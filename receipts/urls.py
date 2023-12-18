from django.urls import path
from . import views
from .views import receipt_list

urlpatterns = [
    path('', receipt_list, name='receipt_list'),

]
