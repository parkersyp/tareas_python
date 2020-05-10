print("Adivina el numero 2.0")

import random

# Debo crear variables adicionales para jugar con bucles:
posibilidades = 5
intentos = 0
limite = 100
adivina = random.randint(1, limite)

nombre = input("Hola, ¿cómo te llamas? ")
print("Muy bien " + nombre + ", el número que estoy pensando es entre 1 y " + str(limite))
print("Tienes " + str(posibilidades) + " posibilidades")

while intentos < posibilidades:
    numero = int(input("Intenta adivinar "))
    if numero == adivina:
        print("GANASTE")
        break
    else:
        intentos += 1
        if intentos < posibilidades and numero > adivina:
            print("Intenta con un número menor")
        elif intentos < posibilidades and numero < adivina:
            print("Intenta con un número mayor")
        else:
            print("PERDISTE")