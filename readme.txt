Serialization: convert complex data into python native data types
Serialization : use for reading data
Json parser : convert serialized data into Json
JsonResponse : convert  serialized data into Json and return JsonResponse
syntax :
1 method: JsonResponse(serialized.data,safe=True);
2 method: serializer=StudentSerializer(stu,many=True)  #serialized data
          json_data=JSONRenderer().render(serializer.data) #json data
By default safe true.
**many shoud be true for multiple data otherwise it will give error
for non dict data it shoud be false otherwise it will give error
desearialization : convert python data into complex data 
desearialization: we used wwhen create,update or delete
syntax: for desearialization first need to convert json data to stream then will to desearialization
  1 Method:   stream=io.BytesIO(json_data)
              python_data=JSONParser().parse(stream) #get python data
              serialize=StudentSerializer(python_data)


For Create API: need to add create function in serializer class
For Update API: need to add update function in serializer class
syntax: update(self,instance,validated_data)
instance: old data
validated_data: new data

DRF Validation: Need to add in Serialization class 
1.Field Level validation :
syntax : def validate_fieldName(self,value):
 def validate_roll(self,value):
      if value >200:
        raise serializers.ValidationError("Seat Full")  # it will raise error you have to print error in view
      return value.

2. Object Level Validation : when need to validate multiple Fields 
syntax: def validate(self,data)

3. Validators: for reusable code throughtout application
eg: DRF5Validation
validation priority : validator->field->object

Model Serializer: shortcut to create serializer class (less code as compare to normal serializer) # same as model forms
* default create and update method implementation
* automatic validation 
* no need to add fields  separatly
 