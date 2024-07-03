from django.shortcuts import render
from .models import Il_Baskanligi , Ilce_Baskanligi
def kurumsal(request):
    return render(request , 'kurumsal.html')

def yk(request):
    return render(request , 'yk.html')

def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def cities(request):
          
    return render(request , 'cities.html')

def bio(request , name):
    return render(request , 'bio.html')

def ib(request , city):

    
    return render(request , 'ib.html')

def ik(request):
    return render(request , 'ik.html')