from django.contrib import admin
from App.models import Student;
# Register your models here.
class StudentData(admin.ModelAdmin):
    list_display=("roll","name","branch")
    
admin.site.register(Student,StudentData);
