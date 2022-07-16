from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Auto


class AutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auto
        fields = '__all__'




 

    


