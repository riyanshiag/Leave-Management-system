from django.urls import path
from . import views

app_name = "main"  

urlpatterns = [
    path('', views.leave_list, name='leave_list'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("dashboard", views.dashboard, name= "dashboard"),
]
 

