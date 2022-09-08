from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student




class StudentSerializer(serializers.ModelSerializer):
    
    # 3 validators : custom validation
    def start_with_a(value):
        if value[0].lower() != 'a':
            raise serializers.ValidationError('Name should be start with A')
    
    name=serializers.CharField(validators=[start_with_a])
    
    class Meta:
        model=Student
        fields='__all__'
    
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
        if nm.lower()=='anamika' and city.lower() !='Bangalore':
            raise serializers.ValidationError('City Must be Bangalore')
        
        return data
        