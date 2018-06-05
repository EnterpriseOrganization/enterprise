from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group



# Create your views here.
from django.http import HttpResponse, JsonResponse
import datetime


def user_login(request):
    print(request.body)
    username = request.POST['username']
    password = request.POST['password']
    print(request.user)
    user = authenticate(request, username=username, password=password)

    status = None
    if user is not None:
        login(request, user)
        print(request.COOKIES)
        print(request.user)
        # print(user.last_login)
        # print(list(Group.objects.filter(user=user))[0].name)
        status = 200
    else:
        status = 422
    response = JsonResponse({'status': status})
    return response


def get_user(request):
    print(request.user)
    user = request.user
    if not user.is_authenticated():
        return JsonResponse({"status ": 404})
    groups = Group.objects.filter(user=user)
    g_list = []
    # print('has perm',user.has_perm('enterprise.add_supplier'))
    # tmp = Supplier(id=3,name="testSupplier",contact="Nothing",phonenumber="11111111",address="NKU")
    # tmp.save()
    for g in groups:
        g_list.append(g.name)
    if request.user.is_authenticated():
        print("authenticated~")
        return JsonResponse({"status": 200,
                             "username": user.username,
                             "firstname": user.first_name,
                             "lastname":  user.last_name,
                             "email": user.email,
                             "lastlogin": user.last_login,
                             "groups": g_list,
                             "datejoined":user.date_joined
                             })
    else:
        return JsonResponse({"status ": 404})


def change_password(request):
    print(request.user)
    userName = request.POST['username']
    oldPassword = request.POST['oldpassword']
    newPassword = request.POST['newpassword']
    user = authenticate(username=userName, password=oldPassword)
    if user is not None:
        user.set_password(newPassword)
        user.save()
        return JsonResponse({'status': 200})
    else:
        return JsonResponse({'status': 400, 'detail': "原密码错误"})


def change_info(request):
    user = User.objects.get(username=request.POST['username'])
    user.email = request.POST['newemail']
    user.last_name = request.POST['newlastname']
    user.first_name = request.POST['newfirstname']
    user.save()
    print(request.user)
    return JsonResponse({'status': 200})


def user_logout(request):
    user = request.user
    if user.is_authenticated():
        logout(request)
        return JsonResponse({"status":200,"detail":"登出成功"})    
    else:
        return JsonResponse({"status":404,"detail":"未登录"})

# def change_names(request):
#     user = User.objects.get(username=request.POST['username'])
#     user.last_name = request.POST['newlastname']
#     user.first_name = request.POST['newfirstname']
#     user.save()
#     print(request.user)
#     return JsonResponse({'status': 200})
