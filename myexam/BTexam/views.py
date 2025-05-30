from django.shortcuts import render
from .models import BTexam

def BTexam_list(request):
    exams = BTexam.objects.filter(is_public=True)
    return render(request, 'BTexam/list.html', {
        'exams': exams,
        'fio': 'Базгудинов Тимур Айдарович',
        'group': 'Группа 231-365'
    })