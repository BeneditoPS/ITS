from django.urls import path
from .views import Index
from django.contrib.auth import views as logar

urlpatterns = [
    path("", Index, name="index"),
    path("login", logar.LoginView.as_view(
        template_name="login.html"
    ), name="login"),
    path("logout", logar.LogoutView.as_view(), name="logout"),
]