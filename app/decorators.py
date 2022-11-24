from django.shortcuts import redirect
from django.core import handlers
def my_login_required(function):
    print("Inside wrapper")
    def wrapper(object, *args, **kwargs):
        print("object is: ")
        print("decorator",object.request.session.get('user_name'))
        if not('user_name' in object.request.session and object.request.session.get('user_name')):
            return redirect('login')
        else:
            return function(object, *args, **kwargs)

    return wrapper