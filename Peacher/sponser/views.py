from django.shortcuts import render
from django.contrib.auth.models import Group
from ideapeacher.models import MyUser
from django.contrib import messages
from django.http import HttpResponse, request

from ideapeacher.forms import CreateUserForm
# Create your views here.


def register_sponser(request):
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