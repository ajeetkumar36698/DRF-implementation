from django.shortcuts import render
from .models import StudentModel
from .serializer import sudentSerializer  # Corrected 'serializer' to 'serializers' and class name
from rest_framework import viewsets  # Corrected 'viewSets' to 'viewsets'

# Create your views here.
class studentViewSet(viewsets.ModelViewSet):  # Corrected class name from 'stustudentViewSet' to 'StudentViewSet'
    queryset = StudentModel.objects.all()
    serializer_class = sudentSerializer  # Corrected 'sudentSerializer' to 'StudentSerializer'
