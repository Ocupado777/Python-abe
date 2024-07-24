def es_palindromo(palabra):
    
    palabra = palabra.lower()
    
    
    if palabra == palabra[::-1]:
        return True
    else:
        return False


def main():
    palabra = input("Escriba la palabra: ")
    
    if es_palindromo(palabra):
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")


if __name__ == "__main__":
    main()

