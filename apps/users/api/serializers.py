from rest_framework import serializers
from apps.users.models import CustomUser

import re

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email', 'nombre', 'apellido_paterno', 'apellido_materno', 'edad', 'telefono', 'is_staff', 'is_active')

class CrearCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'nombre', 'apellido_paterno', 'apellido_materno', 'edad', 'telefono', 'is_staff', 'is_active', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
    def validate_telefono(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("El teléfono debe tener 10 dígitos")
        regex = r'^[0-9]*$'
        if not re.match(regex, value):
            raise serializers.ValidationError("El teléfono debe contener solo números")
        return value

class ActualizarCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'nombre', 'apellido_paterno', 'apellido_materno', 'edad', 'telefono')

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido_paterno = validated_data.get('apellido_paterno', instance.apellido_paterno)
        instance.apellido_materno = validated_data.get('apellido_materno', instance.apellido_materno)
        instance.edad = validated_data.get('edad', instance.edad)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.save()
        return instance
    
    def validate_telefono(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("El teléfono debe tener 10 dígitos")
        regex = r'^[0-9]*$'
        if not re.match(regex, value):
            raise serializers.ValidationError("El teléfono debe contener solo números")
        return value
    
class EliminarCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id')

    def delete(self, instance):
        instance.delete()
        return instance

class OrdenarUsuariosEdad(serializers.Serializer):
    ascendant = serializers.BooleanField()
