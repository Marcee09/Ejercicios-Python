def factorial(num):
    if num==0 or num==1:
        resultado=1
        print({resultado})
    else:
        resultado=num*factorial(num-1)
    return resultado
    

if __name__=='__main__':
    f=int(input("Ingrese un numero para calcular el factorial: "))
    print(f"El factorial es: ",{factorial(f)})
    
        