cadena = input("Introduzca una palabra u oración: ")

totalVocales = {'a': 0,
                'e': 0,
                'i': 0,
                'o': 0,
                'u': 0,
                }

def contadorVocal(vocal, cantidad):
    print("Número total de '{}': {}".format(vocal, cantidad))

# Actualizar número(value) correspondiente a cada vocal(key) en el diccionario
for letra in cadena.lower():
    if (letra == 'a' or letra == 'á'):
        totalVocales['a'] += 1
    elif (letra == 'e' or letra == 'é'):
        totalVocales['e'] += 1
    elif (letra == 'i' or letra == 'í'):
        totalVocales['i'] += 1
    elif (letra == 'o' or letra == 'ó'):
        totalVocales['o'] += 1
    elif (letra == 'u' or letra == 'ú'):
        totalVocales['u'] += 1

# Accesar diccionario y mostrar el número total de cada vocal usando
# la función contadorVocal
for j in totalVocales.keys():
    if (j == 'a'):
        contadorVocal(j, totalVocales[j])
    elif (j == 'e'):
        contadorVocal(j, totalVocales[j])
    elif (j == 'i'):
        contadorVocal(j, totalVocales[j])
    elif (j == 'o'):
        contadorVocal(j, totalVocales[j])
    elif (j == 'u'):
        contadorVocal(j, totalVocales[j])

# Calcular el total de vocales
total = 0
for vocal in totalVocales.keys():
    total += totalVocales[vocal]

print("\nNúmero total de vocales: {}".format(total))
