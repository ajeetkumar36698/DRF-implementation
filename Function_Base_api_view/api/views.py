from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import studentModel
from .serializers import studenSerializer
# Create your views here.
@api_view(['GET',"POST",'PUT',"DELETE",'PATCH'])
def studentView(request,pk=None):
    if(request.method=="GET"):
        id=pk
        if(id is not None):
            stu=studentModel.objects.get(id=id)
            serializer=studenSerializer(stu)
            return Response(serializer.data)
        stu=studentModel.objects.all()
        serializer=studenSerializer(stu,many=True)
        return Response(serializer.data)

     
    if(request.method=="POST"):
        serializer=studenSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'msg':"Data created"})
    if(request.method=="PUT"):
        id=pk
        stu=studentModel.objects.get(id=id)
        serializer=studenSerializer(stu,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'msg':"Complate Data updated"})
        return Response(serializer.errors)
    if(request.method=="PATCH"):
        id=pk
        stu=studentModel.objects.get(id=id)
        serializer=studenSerializer(stu,data=request.data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'msg':"partial Data updated"})
        return Response(serializer.errors)
        
    if(request.method=="DELETE"):
        id=pk
        stu=studentModel.objects.get(id=id)
        stu.delete()
        return Response({'msg':"Data updated"})


