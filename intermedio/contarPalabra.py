def contarPalabra(texto):
    palabras=texto.split()
    diccionario={}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra]+=1
        else:
            diccionario[palabra]=1
    return diccionario


if __name__=='__main__':
    texto=input("Ingresa un texto y te dire la cantidad de palabras iguales: ")
    d=contarPalabra(texto)
    print(d)
