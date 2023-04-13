from django.shortcuts import render
from django.http import JsonResponse
from .models import Log
from django.db.models import Max
#import datetime

# Create your views here.
def index(request):
    maxp= Log.objects.all().aggregate(Max('points'))

    ctx={'maxp':maxp["points__max"]}
    return render (request,"frontend/index.html",ctx)

#def index(request):
    ahora=datetime.datetime.now()
    ctx={"nombre":"Juls","apellidos":"Pasten Da Silva","mail":"A01660665@tec.mx","tiempo":ahora}
    return render(request,"ejemploTheme/index.html",ctx)

def aboutus(request):
    return render(request,"frontend/aboutus.html")

def charts(request):
    maxp=Log.objects.all().aggregate(Max('points'))
    pointList=Log.objects.all().order_by('date')
    ctx={'maxp':maxp["points__max"],"pointList":pointList}
    return render (request,"frontend/charts.html",ctx)

def log(request):
    latest_logs = list(Log.objects.order_by('date')[:5].values())
    return JsonResponse(latest_logs, safe=False)

def hola(request):
    return render(request,' frontend/hola.html')
