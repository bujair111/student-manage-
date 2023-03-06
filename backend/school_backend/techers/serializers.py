from rest_framework import serializers
from .models import Teacher

class TSerializers(serializers.ModelSerializer):
    class Meta :
        model = Teacher
        fields = '__all__' 