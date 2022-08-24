Serializer: convert complex data into python data types
Json parser : convert serialized data into Json
JsonResponse : convert  serialized data into Json and return JsonResponse
syntax : JsonResponse(serialized.data,safe=True);
By default safe true.
for non dict data it shoud be false otherwise it will give error
 