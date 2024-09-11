from django.urls import path
from . import views  # Assuming your views are in the 'registration' app

urlpatterns = [
 
    path('', views.Homepage, name='home'),  # URL for Homepage
    path('login/', views.LoginPage, name='login'),  # URL for LoginPage
    path('signup/', views.SignUpPage, name='signup'),  # URL for SignUpPage
]