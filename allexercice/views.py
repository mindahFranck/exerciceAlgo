from django.shortcuts import render
from django.http import HttpResponse
from sympy import  isprime

# Create your views here.
def homepage(request):
    return render(request, 'index.html')


# redirection vers la page de l'exercice 1
def algorithme1(request):
    return render(request, 'exercice1.html')


# redirection vers la page de l'exercice 2
def algorithme2(request):
    return render(request, 'exercice2.html')


# redirection vers la page de l'exercice 3

def algorithme3(request):
    return render(request, 'exercice3.html')


# fonction de calcul du factoriel prenant en parametre le nombre n

def calculfactorielle(request):
    choix = request.POST.get('options')
    n = int(request.POST.get('nombre'))
    if n >= 0:
        if choix == "factorielle":
            # compte tenu que factiorielle 0 c'est raison pour laquelle ses instructions
            if n == 0:
                return HttpResponse(f'<p>factorielle de {n} est égale a {1} </br> {n}! = {1} </p>')
            else:
                F = 1
                # range cree la liste des nombres qui se trouve entre 2 et n+1 avec n+1 exclu [2, n+1[
                for k in range(2, n + 1):
                    F = F * k
                    print(F)
                return HttpResponse(f'<p>factorielle de {n} est égale a {F} </br> {n}! = {F} </p>')
        else:
            if isprime(n):
                return HttpResponse(f'<p>le nombre {n} est un nombre </br>premier </p>')
            else:
                return HttpResponse(f"<p>le nombre {n} n'est pas  un </br>nombre premier </p>")


    else:
        return HttpResponse(f'<p>Veuillez entrer un nombre</p>')

def add(request):
    users = list()
    note = request.POST.get()
    for i in range(1, 4):
       users.append({"note": note, "matricule": i})

    print(users[1]["noms"])

