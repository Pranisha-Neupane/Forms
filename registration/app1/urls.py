from django.urls import path
from . import views  # Assuming your views are in the 'registration' app
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('', login_required(views.Homepage), name='home'),  # Protect Homepage for logged-in users
    path('login/', views.LoginPage, name='login'),  # URL for LoginPage
    path('signup/', views.SignUpPage, name='signup'),  # URL for SignUpPage
     path('logout/', views.LogoutPage, name='logout'),  # URL for logout functionality
]


