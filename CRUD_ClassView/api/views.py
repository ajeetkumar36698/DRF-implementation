from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import studentSerializer
from .models import studentModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class studentView(View):
    def get(self,request,*args,**kwargs):
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

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=studentSerializer(data=pythondata)
        if(serializer.is_valid()):
            serializer.save()
            res={'msg':"data Created"}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    def put(self,request,*args,**kwargs):
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
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=studentModel.objects.get(id=id)
        stu.delete()
        res={'msg':"data deleted"}
        return JsonResponse(res)









        