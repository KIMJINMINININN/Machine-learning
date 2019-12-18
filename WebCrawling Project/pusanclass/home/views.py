from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db import connection
from base64 import b64encode
from django.core.paginator import Paginator

def index(request):
    return render(request, 'home/index.html')
