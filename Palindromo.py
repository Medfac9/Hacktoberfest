def CheckIfPalindrome(cadena):
    palabra = cadena[::-1]

    if palabra != cadena:
        print("No es palindromo")

    else:
        print("Es palindromo")


CheckIfPalindrome(input("Introduzca una cadena: "))

