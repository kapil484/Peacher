from datetime import datetime
from  ideapeacher.decorators import ideapeacher_only,allowed_users
from django.core.checks import messages
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from .models import MyUser, Public, category, idea
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
    ideas =idea.objects.all()
    comment = Public.objects.all()
    return render(request, "main/home.html",{'idea':ideas,'comments':comment})

@allowed_users(allowed_roles=['sponser'])
def sponserPage(request):
    users = MyUser.objects.all()
    ideas = idea.objects.all()
    comment = Public.objects.all()

    return render(request,"main/homesponser.html",{'ideas':ideas,'users':users,'comments':comment})

@allowed_users(allowed_roles=['ideapeacher'])
def submitIdea(request):
    if request.method == "POST":
        data = request.POST.get("dropdown")

        if category.objects.filter(category=data).exists():
            fdata = category(category=data)
            fdata.save()

            idea1 = request.POST.get("idea")
            user1 = MyUser.objects.get(user = request.user)
            pdf = request.FILES.get('pdf')

            date = datetime.now()

            post = idea(peacher=user1, post_idea = idea1, date_created = date, pdf=pdf)
            post.save()
            post.category.add(fdata)

            return redirect('/home')
        
        else:
            cat=category.objects.get(category=data)

            idea1 = request.POST.get("idea")
            user1 = MyUser.objects.get(user = request.user)
            pdf = request.FILES.get('pdf')

            date = datetime.now()
            post = idea(peacher=user1, post_idea = idea1, date_created = date, pdf=pdf)
            post.save()
            post.category.add(cat)
    
    return redirect("/home")


def post(request):
    return render(request,"main/addidea.html")



def comment(request,pk):
    if request.method == "POST":
        post=idea.objects.get(pk=pk)
        comm=request.POST.get("comment")
        user=request.user
        date=datetime.now()
        data = Public(comment=comm,date_created=date,on_post=post,byUser=user)
        data.save()

    return redirect("/home")

@allowed_users(allowed_roles=['ideapeacher'])
def edit_idea(request,pk):
    id=idea.objects.get(pk=pk)
    context={'edit':id}
    return render(request,"main/edit.html",context)

@allowed_users(allowed_roles=['ideapeacher'])
def updateidea(request,pk):
    ids = idea.objects.get(pk=pk)
    ids.Post_idea = request.POST.get('idea')
    ids.save()
    return redirect("/home")

@allowed_users(allowed_roles=['ideapeacher'])
def delete(request,pk):
    ids=idea.objects.get(pk=pk)
    ids.delete()
    return redirect("/home")