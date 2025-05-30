from django.contrib import admin
from .models import BTexam
from django.contrib.auth.models import User

@admin.register(BTexam)
class ipexamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'exam_date', 'is_public')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'users__email') 
    filter_horizontal = ('users',) 

    date_hierarchy = 'exam_date'