from django.shortcuts import render
from .models import Teacher
from django.http import  JsonResponse
from rest_framework.decorators import api_view
from .serializers import TSerializers

# Create your views here.
@api_view(['POST'])
def add_teacher(request):
    try :
        t_data = request.data
        email_ex = Teacher.objects.filter(t_email = t_data['t_email']).exists()
        if  not email_ex :
            ser_data = TSerializers(data = t_data)
            if ser_data.is_valid():
                ser_data.save()
                msg = 'teacher data added'
            else:
                msg = 'form error'    
        else:
            msg = 'email exist '
    except :
        msg = 'something went wrong'            
    return JsonResponse({'msg':msg})    
