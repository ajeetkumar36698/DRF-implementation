from django.contrib import admin
from .models import studentMode
# Register your models here.
@admin.register(studentMode)
class studentAdmin(admin.ModelAdmin):
    list_display=['name','roll','city']
