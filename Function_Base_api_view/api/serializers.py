from rest_framework import serializers
from .models import studentModel
class studenSerializer(serializers.ModelSerializer):
    class Meta:
        model=studentModel
        fields=['id','name','roll','city']