def es_entero(valor):
    try:
        entero = int(valor)
        if str(entero) == valor:
            return True
        else:
            return False
    except ValueError:
        return False
def es_decimal(valor):
    try:
        float_val = float(valor)
        if '.' in valor:
            return True
        else:
            return False
    except ValueError:
        return False
def mostrar_tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = \033[94m{resultado}\033[0m")  # Resultado en azul
while True:
    entrada = input("Introduce un número entero para mostrar su tabla de multiplicar (o 'salir' para terminar): ")
    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break
    else:
        if es_entero(entrada):
            numero = int(entrada)
            mostrar_tabla_multiplicar(numero)
        elif es_decimal(entrada):
            print("Error: El valor introducido es un número con decimales.")
        else:
            print("Error: El valor introducido no es un número entero válido.")
print("fi del programa")