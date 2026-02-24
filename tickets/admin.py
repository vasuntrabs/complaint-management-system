from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'status', 'created_at')
    list_filter = ('status','created_at')
    search_fields = ('name', 'description', 'email')
    list_editable = ('status',)