from django.shortcuts import render
from .models import Admin
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def admin_login(request):
    username = request.POST['username']
    password = request.POST['password']
    
    try:
        check = Admin.objects.get(a_username = username,a_password = password )
        status = True
    except Exception as e:
        print(e)
        status = False

    return JsonResponse({'status':status})


