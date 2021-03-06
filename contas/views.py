from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Transacao
from .forms import TransacaoForm 
import datetime

def home(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/home.html', data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_home')
    return render(request, 'contas/nova_transacao.html', {'form': form})

def update_transacao(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    return render(request, 'contas/nova_transacao.html', {'form': form})

def delete_transacao(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_home')
