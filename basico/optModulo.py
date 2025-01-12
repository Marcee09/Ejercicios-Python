M = 2701

def compute(n):
    result = 0
    for i in range(1, n + 1):
        result = (result * 10**len(str(n)) + n) % M
    return result

if __name__ == '__main__':
    N1 = 1
    N2 = 2
    N3 = 5
    N4 = 10
    N5 = 20
    N6 = 371844285230994047 % 2701

    print(compute(N1))  
    print(compute(N2))  
    print(compute(N3))  
    print(compute(N4))  
    print(compute(N5))  
    print(compute(N6)) 


