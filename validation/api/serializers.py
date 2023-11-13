from rest_framework import serializers
from .models import studentModel
def start_with_r(value):
    if(value[0].lower()!='r'):
        raise serializers.ValidationError('Name should be start with r')


class studentSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=50,validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=50)
    def create(self,validated_data):
        return studentModel.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    #fields level validation
    # def validate_roll(self,value):
    #     if(value>=200):
    #         raise serializers.ValidationError("seat Full")
    #     return value
    # def validate(self,data):
    #     nm=data.get('name')
    #     ct=data.get('city')
    #     if(nm.lower()=='ajeet' and ct.lower()!='bihar'):
    #         raise serializers.ValidationError("city must be bihar ")
    #     return data



