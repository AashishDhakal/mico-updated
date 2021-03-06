from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',views.LoginView,name='login'),
    path('signup/',views.SignupView,name='signup'),
    path('logout/',views.LogoutView,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),\
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]