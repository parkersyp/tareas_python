print("Calculadora 2.0")

operadores = {
    "=" : "igual",
    "+" : "más",
    "-" : "menos",
    "*" : "por",
    "/" : "entre",
    "//": "entero",
    "**": "elevado",
    "%" : "residuo",
}
while True:
    try:
        num1 = float(input("\nIngresa un número "))
        oper = input("ingresa una operación ")
        num2 = float(input("Ingresa un número "))
        if oper == "+" or oper.lower() == "más":
            print(num1 + num2)
        elif oper == "-" or oper.lower() == "menos":
            print(num1 - num2)
        elif oper == "*" or oper.lower() == "por":
            print(num1 * num2)
        elif oper == "/" or oper.lower() == "entre":
            print(num1 / num2)
        elif oper == "//" or oper.lower() == "entero":
            print(num1 // num2)
        elif oper == "**" or oper.lower() == "elevado":
            print(num1 ** num2)
        elif oper == "%" or oper.lower() == "residuo":
            print(num1 % num2)
        else:
            print("\nEsa operación no es valida")
            print("Solo pueden utilizarse las siguientes:")
            for llaves, valores in operadores.items():
                print(llaves, valores)
    except ValueError:
        print("El caracter ingresado no es válido")
    except ZeroDivisionError:
        print("No puede dividirse entre 0")