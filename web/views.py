from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    return render (request, 'web/home.html')


def librodiario(request):
    response = requests.get('http://127.0.0.1:8000/LibroDiario').json()
    return render(request,'web/librodiario.html', {
        'response':response
    })

def balance(request):
    response = requests.get('http://127.0.0.1:8000/LibroDiario').json()
    return render(request,'web/balance.html', {
        'response':response
    })

def TestBalance(request):
    response = requests.get('http://127.0.0.1:8000/LibroDiario/balanceFechas/2021-06-25/2021-07-10').json()
    return render(request,'web/TestLBalance.html', {
        'response':response
    })