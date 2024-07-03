from django.shortcuts import render
from donations.models import Bagis
from news.models import Haber
def home(request):
    bagislar = Bagis.objects.all()
    haberler = Haber.objects.all() 
    data = {
        'donations' :  bagislar[0:3] , 
        'news' : haberler
    }
    return render(request , 'index.html' , data)
def contact(request):

    return render(request , 'contact.html')
