from rest_framework import serializers
from .models import studentModel
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=studentModel
        fields=['name','roll','city']






