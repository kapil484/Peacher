from django.http.response import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponse("you are not allowed user")
            
        return wrapper_func
    
    return decorator


def ideapeacher_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'ideapeacher':
            return view_func(request, *args, **kwargs)

        elif group == "sponser":
            return HttpResponse("you are not allowed user")
        else:
            return HttpResponse("you are not allowed user")
    return wrapper_func