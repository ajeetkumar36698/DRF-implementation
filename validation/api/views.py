from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import studentSerializer
from .models import studentModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def studentView(request):
    if(request.method=="GET"):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if(id is not None):
            stu=studentModel.objects.get(id=id)
            serializer=studentSerializer(stu)
            return JsonResponse(serializer.data)
        stu=studentModel.objects.all()
        serializer=studentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)
    if(request.method=='POST'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=studentSerializer(data=pythondata)
        if(serializer.is_valid()):
            serializer.save()
            res={'msg':"data Created"}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    if(request.method=='PUT'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=studentModel.objects.get(id=id)
        serializer=studentSerializer(stu,data=pythondata,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            res={'msg':"data updated"}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    if(request.method=="DELETE"):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=studentModel.objects.get(id=id)
        stu.delete()
        res={'msg':"data deleted"}
        return JsonResponse(res)





        