def CheckIfPalindrome(cadena):
    palabra = cadena[::-1]

    if palabra != cadena:
        print("No es palindromo")

    else:
        print("Es palindromo")

def runPal():
	print("\n")
	CheckIfPalindrome(input("Introduzca una cadena: "))
	print("\n")
	from mainMenu import Running
	Running()

