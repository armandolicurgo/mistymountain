import requests
import time
import matplotlib.pyplot as plt
import numpy as np


from pyfiglet import Figlet
f = Figlet(font='slant')
print( f.renderText('Misty Mountain')  )
print("covid19 - graphics  /  Armando Licurgo da Silva\n")


valorestodos,retorno = "",""
maxn,maxx,tipogr = 1,1,""


def dcr():
    global maxn,maxx,tipogr
    q = input("[d]eaths [c]onfirmed [r]recovered: ")
    if q == "d":
        tipogr = 'deaths'
    elif q == "r":
        tipogr = 'recovered'
    elif q=="c":
        tipogr = 'confirmed'
    else:
        exit()
    maxn,maxx = 1,1
    print("")

def url():
    return ('https://pomber.github.io/covid19/timeseries.json') 

def obter():
    global valorestodos
    if valorestodos == "": 
        req = requests.get(url(), timeout=3000)
        valorestodos = req.json()               


def paises():   
    global valorestodos 
    obter()
    retornar=[]
    for pais in valorestodos:
        retornar.append(pais[0:75])
    return retornar

    

def casos(pais,tipogr):
    global maxn, maxx, retorno,valorestodos
    pais = pais.replace("@","a")
    obter()
    retorno = valorestodos[pais]   
    veto = []
    ultimo = 0
    for valores in retorno:
        date = valores['date']
        confirmed = valores['confirmed']
        n = valores[tipogr]
        if confirmed > 0:
            veto.append(n)
            ultimo = date
            maxn = max(maxn,n)
        maxx = max(maxx,len(veto))
    pl0t(pais,veto, ultimo, tipogr)

def pl0t(l4bel,vet, ult, tipog):
    global maxn, maxx, titulo
    plt.title("COVID19 - " + titulo + " - "+ult)
    if tipog == 'deaths':
        plt.ylabel("Mortes")
    elif tipog == 'recovered':
        plt.ylabel("Recuperados")
    else:
        plt.ylabel("Casos confirmados")
    plt.xlabel("Dias apos primeiro caso confirmado")
    plt.grid(True)
    # colocar linestyle
    plt.plot(range(len(vet)), vet,label = l4bel+" "+tipog)
    plt.legend()
    plt.axis([0, int(maxx*1.05), 0, int(maxn*1.05)])


dcr()

todospaises = sorted(paises())
#print(todospaises)
menu = "\n".join(todospaises)[1:]
with open("countries.txt","w") as file:
     file.write(menu)

q=input("[1]Korea Taiwan Japan \n[2]Brasil + Italy + US \n[3]G8+ \n[4]LATAM \n[6]todos \n[7]Brasil\n: ")
if q == "1":
    titulo = "Coreia+Taiwan+Japan+Italia+Espanha+US+Brasil"
    lista1 = "Kore@, South","Taiwan*","Japan","Italy","Spain","US","Brazil" 
elif q == "2":
    titulo = " Brasil + Italy + US + UK + Espanha + Australia "
    lista1 = "Br@zil","US","It@ly","United Kingdom","Spain","Australia"
elif q == "3":
    titulo = " Brasil + G8"
    lista1 = "Brazil","US","Japan","Germany","United Kingdom","France","Italy","Canada"
elif q == "4":
    titulo = " LATAM "
    lista1 = "Brazil","Argentina","Bolivia","Chile","Colombia","Ecuador","Paraguay","Peru", "Uruguay"    #, "French Guiana"
elif q == "6":
    titulo = " Todos os paises "
    lista1 = todospaises
elif q== "7":
    titulo = "Brazil"  #"Netherlands"
else:
    exit()
print("")

if "123456".find(q) > -1:
    for p in lista1:
        casos(p,tipogr)
    plt.show()
elif "7".find(q) > -1:
    casos(titulo,"deaths")
    casos(titulo,"recovered")
    casos(titulo,"confirmed")
    plt.show()

input("digite [enter]")
