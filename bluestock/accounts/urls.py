from django.urls import path
from .views import CustomPasswordResetConfirmView,signup_view, signin_view, CustomPasswordResetView
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView


urlpatterns = [
    path('signup/',signup_view, name='signup'),
    path('signin/',signin_view, name='signin'),
    path('password_reset/',CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
         
]

