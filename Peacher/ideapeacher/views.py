from ideapeacher.decorators import ideapeacher_only
from django.core.checks import messages
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from .models import MyUser, idea
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
        
        if not Group.objects.filter(name='ideapeacher').exists():
            group = Group.objects.create(name='ideapeacher')
            addtogroup = Group.objects.get(name='ideapeacher')
            user.groups.add(addtogroup)

            MyUser.objects.create(user=user,name=user.username)
            messages.success(request, "Account was Created for "+ username)
            return HttpResponse("Created user with group Ideapeacher")
        
        else:
            group = Group.objects.get(name='ideapeacher')
            user.groups.add(group)

            MyUser.objects.create(user=user , name=user.username)
            messages.success(request, "Account was Created for "+ username)
            return HttpResponse("Created user with group Ideapeacher")
    
    context ={'form':form}

    return render(request,'main/register.html',context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return HttpResponse("Login Successful")

        else:
            messages.info(request,'username or password is wrong')

    return render(request,"main/login.html")

def logout_user(request):
    logout(request)
    return redirect('ideapeacher:login_form')


@ideapeacher_only
def ideapeacherpage(request):
    i =idea.objects.all()
    return render(request, "main/home.html",{'idea':i})

