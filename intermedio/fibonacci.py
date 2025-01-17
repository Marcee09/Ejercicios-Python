#0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 ...
def fibonacciForma1(p):
    if p == 0:
        return 0
    elif p == 1 or p == 2:
        return 1
    else:
        a = 0  
        b = 1  
        for i in range(2, p + 1):
            aux = b
            b = a + b  
            a = aux  
        return b


def fibonacciFroma2(p):
    if p==0:
        return p
    if p== 1 or p==2:
        return 1
    else:
        return fibonacciFroma2(p-1)+fibonacciFroma2(p-2)
    
    


if __name__=='__main__':
    pos=int(input("Ingresa una posicion para ver el valor correspondiente: "))
    f=fibonacciForma1(pos)
    print("el valor fibonacci en esa posicion es :",f)
    f2=fibonacciFroma2(pos)
    print("El valor de fibonacci calculado con recursividad :",f2)