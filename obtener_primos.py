from math import sqrt, floor

def obtener_primos(n):
    """
    Dado un numero entero positivo, devuelve
    una lista con todos los primos hasta dicho
    número inclusive
    """
    primos = [True for _ in range(n+1)]
    for i in range(2,floor(sqrt(n))):
        if primos[i]:
            for j in range(i**2,n+1,i):
                primos[j] = False
    return [i for i in range(2,n+1) if primos[i]]

print(obtener_primos(99))
