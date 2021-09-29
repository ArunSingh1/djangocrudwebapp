from attr import field
from rest_framework import serializers
from .models import Cars


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'
        #field = ['id', 'carname', 'carcompany', 'driveline','geartype']

    def create(self, validated_data):
        return Cars.objects.create(**validated_data)