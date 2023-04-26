from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFOD=TopicForm(request.POST)
        if TFOD.is_valid():
            TFOD.save()
            return HttpResponse('Topic is inserted')
        else:
            return HttpResponse(' Topic data is not valid')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}

    if request.method=='POST':
        WFOD=WebpageForm(request.POST)
        if WFOD.is_valid():
            WFOD.save()
            return HttpResponse('Webpage data enterd successfully')
        else:
            return HttpResponse('Webpage data is not valid')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    ARO=AccessrecordForm()
    d={'ARO':ARO}

    if request.method=='POST':
        AROD=AccessrecordForm(request.POST)
        if AROD.is_valid():
            AROD.save()
            return HttpResponse('inserted Accessrecords data successfully')
        else:
            return HttpResponse('Accessrecords data is not valid')


    return render(request,'insert_access.html',d)