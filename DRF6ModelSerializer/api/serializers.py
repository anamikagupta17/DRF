from attr import fields
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # for readonly
    #name=serializers.CharField(read_only=True) # for single text
    
    class Meta:
        model=Student
        #fields=['name','roll','city']
        fields='__all__'
        #read_only_fields=['name','city']  #to make multiple fileds readonly
        
        #extra aruguments like read only,write only,required... can do like this also
        
        #extra_kwargs={'name':{'read_only':True}}
        


