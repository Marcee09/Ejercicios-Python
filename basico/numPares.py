def pares(inicio,fin):
    pares=[]
    i=inicio
    for i in range(inicio,fin):
        if i%2==0:
            pares.append(i)
    return pares

if __name__=='__main__':
    print("Encontrare los numeros pares de un rango dado")
    ini=int(input("Ingrese el numero inicial: "))
    fin=int(input("Ingrese el numero final del rango: "))
    p=pares(ini,fin)
    print("Los numeros pares del rango son: ",p)


