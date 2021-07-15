from django.urls import path
from . import views

app_name='ideapeacher'

urlpatterns = [
    path('registerPeacher/',views.register_user, name='register_form'),
    path('loginPeacher/',views.login_user,name='login_form'),
    path('logoutPeacher/',views.logout_user,name='logout_form'),
    path('home/',views.ideapeacherpage,name='home')
]