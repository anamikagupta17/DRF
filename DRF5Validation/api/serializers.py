from rest_framework import serializers
from .models import Student

# 3 validators
def start_with_r(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError('Name should be start with A')


class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50, validators=[start_with_r])
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
    
    # 1 field level validation
    
    def validate_roll(self,value): #when is_valid run that time this function will call
        if value >200:
            raise serializers.ValidationError("Seat Full")  # it will raise error you have to print error in view
        return value
    
    
    
    # 2 object Level validation
    
    def validate(self, data):
        print(data)
        nm=data.get('name')
        city=data.get('city')
        if nm.lower()=='mansi' and city !='gola':
            raise serializers.ValidationError('City Must be Gola')
        
        return data
        