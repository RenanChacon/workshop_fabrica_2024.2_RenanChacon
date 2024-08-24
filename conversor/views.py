from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
cotacao_dolar = float(cotacoes['USDBRL']['bid'])
cotacao_euro = float(cotacoes['EURBRL']['bid'])
cotacao_bitcoin = float(cotacoes['BTCBRL']['bid'])

def converter_real(valor_real,moeda):
    if moeda == "dolar":
        resultado = valor_real / cotacao_dolar
    elif moeda == "euro":
        resultado = valor_real / cotacao_euro
    elif moeda == "bitcoin":
        resultado = valor_real / cotacao_bitcoin
    
    return round(resultado,2)

def converter_para_real(valor_moeda,moeda):
    if moeda == "dolar":
        resultado = valor_moeda * cotacao_dolar
    elif moeda == "euro":
        resultado = valor_moeda * cotacao_euro
    elif moeda == "bitcoin":
        resultado = valor_moeda * cotacao_bitcoin
    
    return resultado

def mostrar_conversor(request):
    if request.method == "GET":
        return render(request, 'conversor.html', {'dolar': cotacao_dolar, 
        'euro': cotacao_euro, 'bitcoin': cotacao_bitcoin})
    
    elif request.method == "POST":
        escolha = request.POST.get('conversao')
        valor = float(request.POST.get('valor'))
        
        if escolha == "real_dolar":
            resultado = converter_real(valor,"dolar")
        elif escolha == "real_euro":
            resultado = converter_real(valor,"euro")
        elif escolha == "real_bitcoin":
            resultado = converter_real(valor,"bitcoin")
        elif escolha == "dolar_real":
            resultado = converter_para_real(valor,"dolar")
        elif escolha == "euro_real":
            resultado = converter_para_real(valor,"euro")
        elif escolha == "bitcoin_real":
            resultado = converter_para_real(valor,"bitcoin")
        
        return render(request, 'resultado_conversao.html', {'resultado': resultado})
    
def mostrar_resultado(request, resultado):
    return render(request,'resultado_conversao.html', {'resultado': resultado})
