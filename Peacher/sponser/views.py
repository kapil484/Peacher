from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponse, request
from .models import SponerUser

from ideapeacher.forms import CreateUserForm
# Create your views here.


def register_sponser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
        
            if not Group.objects.filter(name='sponser').exists():
                group = Group.objects.create(name='sponser')
                addtogroup = Group.objects.get(name='sponser')
                user.groups.add(addtogroup)

                SponerUser.objects.create(user=user,name=user.username)
                messages.success(request, "Account was Created for "+ username)
                return HttpResponse("Created user with group sponser")
            
            else:
                group = Group.objects.get(name='sponser')
                user.groups.add(group)

                SponerUser.objects.create(user=user , name=user.username)
                messages.success(request, "Account was Created for "+ username)
                return HttpResponse("Created user with group sponser")
        
    context ={'form':form}

    return render(request,'main/register.html',context)