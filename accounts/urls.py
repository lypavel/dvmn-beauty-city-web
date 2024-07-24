from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import authorize_user

app_name = 'accounts'

urlpatterns = [
    path('authorize', authorize_user, name='authorize'),
]

urlpatterns += [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
