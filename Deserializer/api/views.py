from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

# Create your views here.
def student_create(requests):
    if(requests.method=="POST"):
        json_data=requests.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=studentserializer(data=pythondata)
        if(serializer.is_valid()):
            serializer.save()
            res={'msg':'data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)  
        return HttpResponse(json_data,content_type='application/json')

