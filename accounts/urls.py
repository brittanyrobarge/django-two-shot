from django.urls import path, include
from .views import login_view, custom_logout, signup_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('signup/', signup_view, name='signup'),
]
