Serialization: convert complex data into python native data types
Serialization : use for reading data
Json parser : convert serialized data into Json
JsonResponse : convert  serialized data into Json and return JsonResponse
syntax :
1 method: JsonResponse(serialized.data,safe=True);
2 method: serializer=StudentSerializer(stu)  #serialized data
          json_data=JSONRenderer().render(serializer.data) #json data
By default safe true.
for non dict data it shoud be false otherwise it will give error
desearialization : convert python data into complex data 
desearialization: we used wwhen create,update or delete
syntax: for desearialization first need to convert json data to stream then will to desearialization
  1 Method:   stream=io.BytesIO(json_data)
              python_data=JSONParser().parse(stream) #get python data
              serialize=StudentSerializer(python_data)


 