from django.contrib import admin
from .models import Admission

# Register your models here.

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course', 'created_at']
    search_fields = ['name', 'email']