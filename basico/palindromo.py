def palindromo(palabra):
    largo=len(palabra)
    invertida=''
    i=0
    while i<largo:
        invertida+=palabra[largo-1]
        largo-=1
    if invertida==palabra:
        print("La palabra que ingresaste es palindromo")
    else:
        print("La palabra que ingresaste no es palindromo")

if __name__=='__main__':
    pal=input("Ingresa una palabra y te diré si es palindromo: ")
    palindromo(pal)