from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    html = f"<html><body>Agora é {now}</body></html>"
    return HttpResponse(html)
