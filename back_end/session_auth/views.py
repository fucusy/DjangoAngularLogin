from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
# Create your views here.
from session_auth.serializers import UserSerializer
from rest_framework import status

@api_view(('GET','POST'))
def login(request,username,password):
    user = authenticate(username=username, password=password)

    res = {'res': 0, "msg": ""}

    if user is not None:
        if user.is_active:
            auth_login(request, user)
            res['res'] = 1
            res['msg'] = "login success"
        else:
            res['res']= 0
            res['msg'] = "have not active"
    else:
        res['res'] = 0
        res['msg'] = "username or password is error"
    return Response(res)

@api_view(('GET','POST'))
def get_profile(request):
    if request.user.is_authenticated():
        serializer = UserSerializer(request.user, many=False)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(('GET','POST'))
def logout(request):
    auth_logout(request)
    res = {'res':1}
    return Response(res)