from django.urls import path
from . import views

app_name='ideapeacher'

urlpatterns = [
    path('registerPeacher/',views.register_user, name='register_form'),
    path('loginPeacher/',views.login_user,name='login_form'),
    path('logoutPeacher/',views.logout_user,name='logout_form'),
    path('home/',views.ideapeacherpage,name='home'),
    path('homesponser/',views.sponserPage,name='home_sponser'),
    path('submitIdeas/',views.submitIdea, name='submitidea'),
    path('idea/',views.post, name='idea'),
    path('comment/<int:pk>/',views.comment, name='comment'),
    path('edit_idea/<int:pk>/',views.edit_idea, name='edit_idea'),
    path('updateidea/<int:pk>/',views.updateidea, name='updateidea'),
    path('delete/<int:pk>/',views.delete, name='delete'),
]

