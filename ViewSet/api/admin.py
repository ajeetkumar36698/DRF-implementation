from django.contrib import admin
from .models import StudentModel
# Register your models here.
@admin.register(StudentModel)
class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','email']
