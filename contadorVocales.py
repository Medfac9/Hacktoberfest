def CountVowels(cadena):
    contador = 0
    contadorA = 0
    contadorE = 0
    contadorI = 0
    contadorO = 0
    contadorU = 0

    for i in cadena:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            contador+=1
            if(i == 'a'):
                contadorA+=1
            elif(i == 'e'):
                contadorE+=1
            elif(i == 'i'):
                contadorI+=1
            elif(i == 'o'):
                contadorO+=1
            elif(i == 'u'):
                contadorU+=1



    print("Numero total de vocales:", contador)
    print("Numero total de 'a':", contadorA)
    print("Numero total de 'e':", contadorE)
    print("Numero total de 'i':", contadorI)
    print("Numero total de 'o':", contadorO)
    print("Numero total de 'u':", contadorU)

def runCon():
    string = input("Introduzca una cadena: ")
    CountVowels(string)
    print("\n")
    from mainMenu import Running
    Running()

