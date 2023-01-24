from django.shortcuts import render
from app.models import *
# Create your views here.
def display_Topic(request):

    QST=Topic.objects.all()
    d={'topics':QST}

    return render(request,'display_Topic.html',d)



def display_Webpage(request):
    QSW=Webpage.objects.all()
    d={'names':QSW}

    return render(request,'display_Webpage.html',d)
    


def display_AccessRecords(request):

    QSA=AccessRecord.objects.all()
    d={'access':QSA}
    return render(request,'display_AccessRecords.html',d)   