from rest_framework import serializers
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Usuarios
        fields = '__all__'
