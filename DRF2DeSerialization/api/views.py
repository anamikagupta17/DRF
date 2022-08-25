from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt  # to avoid csrf error
def student_create(req):
    if req.method=='POST':
        json_data=req.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream) #get python data
        serialize=StudentSerializer(data=python_data) # convert to complex data
        if serialize.is_valid():
            serialize.save()
            res={'msg':'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        # in case if any error
        # 1st method
        #json_data=JSONRenderer().render(serialize.errors)
        #return HttpResponse(json_data,content_type='application/json')
        
        # 2nd method
        return JsonResponse(json_data)