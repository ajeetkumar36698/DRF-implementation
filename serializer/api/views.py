from django.shortcuts import render
from .models import studentModel
from .serializers import studentSerializer
from django.http import JsonResponse
# Create your views here.
def studentView(request,pk):
    stu=studentModel.objects.get(id=pk)
    serializer=studentSerializer(stu)
    return JsonResponse(serializer.data)
def studentDetailsView(request):
    stu=studentModel.objects.all()
    serializer=studentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)