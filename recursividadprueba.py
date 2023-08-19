#Calculando el factorial de un numero utilizando Recursividad
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
    num = 5
    print(f"El Factorial de {num} es {factorial(num)}")
