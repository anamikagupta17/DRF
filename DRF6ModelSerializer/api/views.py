from django.shortcuts import render
from uritemplate import partial
from yaml import serialize
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.



@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self,req,*args,**kwargs):
        json_data=req.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        # if id none
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        print(serializer)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')   



    def post(self,req,*args,**kwargs):
        json_data=req.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Inserted'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def put(self,req,*args,**kwargs):
        json_data=req.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        #serializer=StudentSerializer(stu,data=python_data) #full data update
        serializer=StudentSerializer(stu,data=python_data,partial=True) #partial true when only few data getting update
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    
    def delete(self,req,*args,**kwargs):
        json_data=req.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')  
        stu=Student.objects.get(id=id)  
        stu.delete()  
        res={'msg':'Data Deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')  
        
        