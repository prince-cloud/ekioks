from django.urls import path
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from . import views
#from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name="register"),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset-done'),
]  
