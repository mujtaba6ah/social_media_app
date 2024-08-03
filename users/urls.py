from django.urls import path
from . import views
from django.contrib.auth import logout
from django.contrib.auth import views as auth_view

urlpatterns = [
    
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('',views.index,name='index'),
    path('password_change',auth_view.PasswordChangeView.as_view(template_name='users/password_change_form.html'),name='password_change'),
    path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),name='pasword_reset'),
    path('password_reset/',auth_view.PasswordChangeDoneView.as_view(template_name='users/password_reset_done.html'),name='pasword_reset_done'),
    path('users/password_reset/confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password/reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path("reset/done",auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),
    path('register/',views.register, name='register'),

    #path('logout/',auth_view.LogoutView.as_view(template_name='/Users/mujtabaabdelgadir/Desktop/social/socialproject/users/templates/users/logout.html'),name='logout'),
    
]