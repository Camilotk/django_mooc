from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Transacao
import datetime

def home(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/home.html', data)
