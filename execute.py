from printPrimes import printPrimes  # isPrime(number)
from Adivina import runAdivina
from contadordeVocales2 import runCon2
from contadorVocales import runCon
from expRegulares import compruebaExpresiones
from hcf import runHcf
from obtener_primos import runObt
from Palindromo import runPal

def printOut(choice):
    # print(choice)
    if choice == '1':
    	printPrimes()
    elif choice == '2':
    	runAdivina()
    elif choice == '3':
    	runCon2()
    elif choice == '4':
    	runCon()
    elif choice == '5':
    	compruebaExpresiones()
    elif choice == '6':
    	runHcf()
    elif choice == '7':
    	runObt()
    elif choice == '8':
    	runPal()