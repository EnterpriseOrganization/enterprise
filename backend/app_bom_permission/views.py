from django.shortcuts import render
from django.contrib.auth import authenticate, login ,logout


# Create your views here.
from django.http import HttpResponse,JsonResponse
import datetime

def user_login(request):
    print(request.body)
    username = request.POST['username']
    password = request.POST['password']
    # username = 'qw'
    # password = 'qw123456'
    print(request.user)
    user = authenticate(request, username=username, password=password)

    print(request.COOKIES)
    # print(get_user(request))
    status=None
    if user is not None:
        login(request, user)
        print(request.COOKIES)
        print(request.user)
        status=200
    else:
        status=422
    response = JsonResponse({'status':status})
    return response

def get_user(request):
    return JsonResponse({})
    

def change_password(request):
    print(request.user)
    user = request.user
    user

# def get_user(request):
#     from django.contrib.auth.models import AnonymousUser
#     try:
#         user_id = request.session['SESSION_KEY']
#         backend_path = request.session['BACKEND_SESSION_KEY']
#         backend = load_backend(backend_path)
#         user = backend.get_user(user_id) or AnonymousUser()
#     except KeyError:
#         user = AnonymousUser()
#     return user