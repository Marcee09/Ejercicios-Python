#0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 ...
def fibonacciForma1(p):
    if p==0:
        return p
    elif p==1 or p==2:
        return 1
    else:
        a=0 #0,1,1,2,3
        b=1 #1,1,2,3,5
        for i in range(2,p):
            a=b
            b=a+b
        return a


if __name__=='__main__':
    pos=int(input("Ingresa una posicion para ver el valor correspondiente: "))
    f=fibonacciForma1(pos)
    print("el valor fibonacci en esa posicion es :",f)