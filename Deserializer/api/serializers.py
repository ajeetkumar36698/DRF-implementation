from rest_framework import serializers
from .models import studentMode
class studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=50)
    def create(self,validate_data):
        return studentMode.objects.create(**validate_data)
