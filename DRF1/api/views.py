import imp
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.

#Model obeect - Single bject data

def student_details(req):
    stu=Student.objects.get(id=2) #model object -complex data
    print(stu)
    serializer=StudentSerializer(stu) # serialized data (python object data)
    print(serializer)
    print(serializer.data)
    json_data=JSONRenderer().render(serializer.data) # json data
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')

def student_details_byId(req,pk):
    stu=Student.objects.get(id=pk) #model object -complex data
    serializer=StudentSerializer(stu) # serialized data
    #1st method
    #json_data=JSONRenderer().render(serializer.data) # json data
    #return HttpResponse(json_data,content_type='application/json')

    #2nd method
    return JsonResponse(serializer.data) #convert and return data

# Query Set: All student data
def student_list(req):
    stu=Student.objects.all() #query set -complex data
    print(stu)
    serializer=StudentSerializer(stu,many=True) # serialized data,many for multiple data
    print(serializer)
    print(serializer.data)
    json_data=JSONRenderer().render(serializer.data) # json data
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')
