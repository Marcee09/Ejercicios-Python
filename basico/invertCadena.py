
def invertirCadena(cadena):
    largo=len(cadena)
    cadenaInvertida= ''
    i=0
    while i< len(cadena):
        cadenaInvertida+=cadena[largo-1]
        largo-=1
        i+=1
    return cadenaInvertida


if __name__=='__main__':
    cadena=input("Ingresa un texto y te muestro el texto innvertido: ")
    c=invertirCadena(cadena)
    print("El texto invertido queda: ",c)