
from django.urls import path
from .views import LoginView, CheckAuthView, LogoutView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('check-auth/', CheckAuthView.as_view(), name='check-authentication'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
]