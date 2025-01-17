def criterio_de_ordenacion(item):
    return item[1]  # Devuelve el valor (segundo elemento de la tupla) como criterio de ordenación.

def ordenarDiccionario(diccionario):
    # diccionario.items() -> Genera un iterable de tuplas (clave, valor) a partir del diccionario.
    # sorted() -> Ordena estas tuplas según el criterio de ordenación, por defecto de menor a mayor.
    # key=criterio_de_ordenacion -> Define que la ordenación se hará utilizando el valor de cada tupla (item[1]).
    # La comprensión de diccionario (estructura especial) recorre las tuplas ordenadas y reconstruye un nuevo diccionario con las claves y valores ordenados.
    ordenado = {k: v for k, v in sorted(diccionario.items(), key=criterio_de_ordenacion)}
    return ordenado

if __name__ == '__main__':
    try:
        diccionario = eval(input("Ingresa un diccionario de la forma {'a': 3, 'b': 1, 'c': 2} y lo ordeno de menor a mayor: "))
        
        # Verificamos que la entrada sea un diccionario válido antes de procesarlo.
        if isinstance(diccionario, dict):
            print("Diccionario ordenado: ", ordenarDiccionario(diccionario))
        else:
            print("La entrada no es un diccionario válido.")
    except (SyntaxError, NameError):
        print("La entrada no es un diccionario válido.")




