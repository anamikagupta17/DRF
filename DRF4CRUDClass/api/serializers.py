from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
    
    
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):  #instance : old data,Vaidated_data: New data
        print(instance)
        instance.name=validated_data.get('name',instance.name) # if name didnt chnage then it will take old name
        instance.roll=validated_data.get('roll',instance.roll)
        print(instance.name)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    