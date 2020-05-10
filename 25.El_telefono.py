print("\nEjericio: El telefono \n")

import random
import time
import datetime
bucle1 = 0
while bucle1 == 0:
    origenes = ["SAL", "GTY", "MEX", "USA"]
    destinos = origenes
    categorias = ["70 lbs", "100 lbs"]
    maletas = ["50 lbs", "70 lbs","100 lbs"]
    monedas = ["Dolares", "Colones", "Quetzales", "Pesos"]
    medios = ["Chat", "Telefono", "Counter"]
    bucle2 = 10
    print("Bienvenido a Avianca, por favor elija el número para la elección que desea ejecutar \n")
    menu = (
        "Oprima 1, si quiere información de su boleto",
        "Oprima 2, si quiere cambios en su boleto",
        "Oprima 3, si quiere comprar un nuevo boleto",
        "Oprima 4, si quiere comprar equipaje extra",
        "Oprima 5, si quiere recibir créditos fiscales",
        "Oprima 6, si quiere poner un reclamo",
        "Oprima 7, si quiere información general",
        "Oprima 8, si quiere volver a escuchar el menú",
        "Oprima 9, si quiere salir de la llamada"
    )
    for opcion in menu:
        print(opcion)
    num = int(input("> "))
    if num == 1:
        bucle2 += num
        while bucle2 == 11:
            boleto = input("Favor ingrese su número de boleto ")
            correo = input("Favor ingrese su correo electronico ")
            arroba = "@"
            punto = "."
            if arroba and punto not in correo:
                print("El correo electronico introducido no existe")
                print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                num5 = int(input("> "))
                if num5 == 8:
                    break
                if num5 == 9:
                    bucle1 += 1
                    print("Gracias por volar con nosotros")
                    break
            else:
                print("Su itinerario del boleto " + boleto + " ha sido enviado al correo " + correo)
                bucle2 -= num
                print("Oprima 8 para volver al menu principal o 9 para salir de la llamada")
                num2 = int(input("> "))
                if num2 == 8:
                    break
                if num2 == 9:
                    bucle1 += 1
                    print("Gracias por volar con nosotros")
                    break
    if num == 2:
        bucle2 += num
        while bucle2 == 12:
            print("Oprima 1 para cancelar su viaje")
            print("Oprima 2 para cambiar la fechas de su viaje")
            num2 = int(input("> "))
            if num2 == 1:
                boleto = input("Favor ingrese su número de boleto ")
                print("Esta seguro que quiere cancelar el boleto " + boleto +". Si esta seguro presione 1, sino presione 2")
                confirmacion = int(input("> "))
                if confirmacion == 1:
                    cancelacion = random.randint(10000,99999)
                    print("El número de boleto " + boleto + " ha sido cancelado")
                    print("Su número de transacción es " + str(cancelacion))
                    print("Oprima 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        bucle1 += 1
                        print("Gracias por volar con nosotros")
                        break
                else:
                    print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
            elif num2 == 2:
                boleto = input("Favor ingrese su número de boleto ")
                fecha_salida = input("Digite la nueva fecha de salida de su viaje en formato mm/dd/aaaa ")
                posicion2_salida = fecha_salida[2]
                posicion5_salida = fecha_salida[5]
                posicion9_salida = fecha_salida[6:10]
                año_actual = int(time.strftime("%Y"))
                if posicion2_salida and posicion5_salida != "/":
                    print("la fecha de salida es erronea o no cumple el formato")
                    print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                elif int(posicion9_salida) < año_actual:
                    print("la fecha de salida es anterior a la actual")
                    print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                else:
                    mes_salida = int(fecha_salida[0:2])
                    dia_salida = int(fecha_salida[3:5])
                    if mes_salida > 12 or dia_salida > 31:
                        print("la fecha de salida es erronea o no cumple el formato")
                        print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                        num2 = int(input("> "))
                        if num2 == 8:
                            break
                        if num2 == 9:
                            print("Gracias por volar con nosotros")
                            bucle1 += 1
                            break
                    else:
                        fecha_salida_format = datetime.datetime.strptime(fecha_salida, "%m/%d/%Y")
                        fecha_regreso = input("Digite la nueva fecha de regreso de su viaje en formato mm/dd/aaaa ")
                        posicion2_regreso = fecha_regreso[2]
                        posicion5_regreso = fecha_regreso[5]
                        posicion9_regreso = fecha_regreso[6:10]
                        if posicion2_regreso and posicion5_regreso != "/":
                            print("la fecha de regreso es erronea o no cumple el formato")
                            print("Oprima 0 para volver al sub-menu,8 para volver al menu principal o 9 para salir de la llamada")
                            num2 = int(input("> "))
                            if num2 == 8:
                                break
                            if num2 == 9:
                                print("Gracias por volar con nosotros")
                                bucle1 += 1
                                break
                        elif int(posicion9_regreso) < año_actual:
                            print("la fecha de regreso es anterior a la actual")
                            print("Oprima 0 para volver al sub-menu,8 para volver al menu o 9 para salir de la llamada")
                            num2 = int(input("> "))
                            if num2 == 8:
                                break
                            if num2 == 9:
                                print("Gracias por volar con nosotros")
                                bucle1 += 1
                                break
                        else:
                            mes_regreso = int(fecha_regreso[0:2])
                            dia_regreso = int(fecha_regreso[3:5])
                            if mes_regreso > 12 or dia_regreso > 31:
                                print("la fecha de regreso es erronea o no cumple el formato")
                                print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                                num2 = int(input("> "))
                                if num2 == 8:
                                    break
                                if num2 == 9:
                                    print("Gracias por volar con nosotros")
                                    bucle1 += 1
                                    break
                            else:
                                fecha_regreso_format = datetime.datetime.strptime(fecha_regreso, "%m/%d/%Y")
                                if fecha_salida_format == fecha_regreso_format:
                                    print("Operación invalida, la fecha de regreso no puede ser la misma fecha de salida")
                                    print("Oprima 0 para volver al sub-menu,8 para volver al menu principal o 9 para salir de la llamada")
                                    num2 = int(input("> "))
                                    if num2 == 8:
                                        break
                                    if num2 == 9:
                                        print("Gracias por volar con nosotros")
                                        bucle1 += 1
                                        break
                                elif fecha_regreso_format < fecha_salida_format:
                                    print("Operación invalida, la fecha de regreso no puede ser anterior a la fecha de salida")
                                    print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                                    num2 = int(input("> "))
                                    if num2 == 8:
                                        break
                                    if num2 == 9:
                                        print("Gracias por volar con nosotros")
                                        bucle1 += 1
                                        break
                                else:
                                    print("El número de boleto " + boleto + "ha sido modificado a la fecha de salida " + fecha_salida + " y la fecha de regreso " + fecha_regreso)
                                    transaccion = random.randint(10000, 99999)
                                    print("Su número de transacción es " + str(transaccion))
                                    print("Oprima 8 para volver al menu o 9 para salir de la llamada")
                                    num2 = int(input("> "))
                                    if num2 == 8:
                                        break
                                    if num2 == 9:
                                        print("Gracias por volar con nosotros")
                                        bucle1 += 1
                                        break
            else:
                print("la opción elegida no es válida")
                print("Oprima 8 para volver al menu o 9 para salir de la llamada")
                num2 = int(input("> "))
                if num2 == 8:
                    break
                if num2 == 9:
                    bucle1 += 1
                    break
    if num == 3:
        bucle2 += num
        while bucle2 == 13:
            print("Los origenes disponibles son: " + str(origenes))
            origen = input("Escriba origen del vuelo ")
            origen = origen.upper()
            if origen not in origenes:
                print("El origen introducido no es válido")
                print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                num2 = int(input("> "))
                if num2 == 8:
                    break
                if num2 == 9:
                    print("Gracias por volar con nosotros")
                    bucle1 += 1
                    break
            else:
                print("Los destinos disponibles son: " + str(destinos))
                destino = input("Escriba destino del vuelo ")
                destino = destino.upper()
                if destino not in destinos:
                    print("El destino introducido no es válido")
                    print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                elif origen == destino:
                    print("Operación invalida, el origen y el destino no pueden ser el mismo")
                    print("Oprima 0 para volver a empezar,8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                else:
                    fecha_salida = input("Digite la fecha de salida del vuelo en formato mm/dd/aaaa ")
                    posicion2_salida = fecha_salida[2]
                    posicion5_salida = fecha_salida[5]
                    posicion9_salida = fecha_salida[6:10]
                    año_actual = int(time.strftime("%Y"))
                    if posicion2_salida and posicion5_salida != "/":
                        print("la fecha de salida es erronea o no cumple el formato")
                        print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                        num2 = int(input("> "))
                        if num2 == 8:
                            break
                        if num2 == 9:
                            print("Gracias por volar con nosotros")
                            bucle1 += 1
                            break
                    elif int(posicion9_salida) < año_actual:
                        print("la fecha de salida es anterior a la actual")
                        print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                        num2 = int(input("> "))
                        if num2 == 8:
                            break
                        if num2 == 9:
                            print("Gracias por volar con nosotros")
                            bucle1 += 1
                            break
                    else:
                        mes_salida = int(fecha_salida[0:2])
                        dia_salida = int(fecha_salida[3:5])
                        if mes_salida > 12 or dia_salida > 31:
                            print("la fecha de salida es erronea o no cumple el formato")
                            print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                            num2 = int(input("> "))
                            if num2 == 8:
                                break
                            if num2 == 9:
                                print("Gracias por volar con nosotros")
                                bucle1 += 1
                                break
                        else:
                            fecha_salida_format = datetime.datetime.strptime(fecha_salida, "%m/%d/%Y")
                            fecha_regreso = input("Digite la fecha de regreso del vuelo en formato mm/dd/aaaa ")
                            posicion2_regreso = fecha_regreso[2]
                            posicion5_regreso = fecha_regreso[5]
                            posicion9_regreso = fecha_regreso[6:10]
                            if posicion2_regreso and posicion5_regreso != "/":
                                print("la fecha de regreso es erronea o no cumple el formato")
                                print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                                num2 = int(input("> "))
                                if num2 == 8:
                                    break
                                if num2 == 9:
                                    print("Gracias por volar con nosotros")
                                    bucle1 += 1
                                    break
                            elif int(posicion9_regreso) < año_actual:
                                print("la fecha de regreso es anterior al actual")
                                print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                                num2 = int(input("> "))
                                if num2 == 8:
                                    break
                                if num2 == 9:
                                    print("Gracias por volar con nosotros")
                                    bucle1 += 1
                                    break
                            else:
                                mes_regreso = int(fecha_regreso[0:2])
                                dia_regreso = int(fecha_regreso[3:5])
                                if mes_regreso > 12 or dia_regreso > 31:
                                    print("la fecha de regreso es erronea o no cumple el formato")
                                    print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                                    num2 = int(input("> "))
                                    if num2 == 8:
                                        break
                                    if num2 == 9:
                                        print("Gracias por volar con nosotros")
                                        bucle1 += 1
                                        break
                                else:
                                    fecha_regreso_format = datetime.datetime.strptime(fecha_regreso, "%m/%d/%Y")
                                    if fecha_salida_format == fecha_regreso_format:
                                        print("Operación invalida, la fecha de regreso no puede ser la misma fecha de salida")
                                        print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                                        num2 = int(input("> "))
                                        if num2 == 8:
                                            break
                                        if num2 == 9:
                                            print("Gracias por volar con nosotros")
                                            bucle1 += 1
                                            break
                                    elif fecha_regreso_format < fecha_salida_format:
                                        print("Operación invalida, la fecha de regreso no puede ser anterior a la fecha de salida")
                                        print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                                        num2 = int(input("> "))
                                        if num2 == 8:
                                            break
                                        if num2 == 9:
                                            print("Gracias por volar con nosotros")
                                            bucle1 += 1
                                            break
                                    else:
                                        correo = input("Favor ingrese su correo electonico: ")
                                        arroba = "@"
                                        punto = "."
                                        if arroba and punto not in correo:
                                            print("El correo electronico introducido no existe")
                                            print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                                            num2 = int(input("> "))
                                            if num2 == 8:
                                                break
                                            if num2 == 9:
                                                print("Gracias por volar con nosotros")
                                                bucle1 += 1
                                                break
                                        else:
                                            recibo = random.randint(10000, 99999)
                                            print("Su boleto de "+ origen + " a " + destino + " con fechas de "+fecha_salida + " a " + fecha_regreso + " ha sido enviado al correo " + correo)
                                            print("Su número de transacción es: " + str(recibo))
                                            print("Oprima 8 para volver al menu principal o 9 para salir de la llamada")
                                            num2 = int(input("> "))
                                            if num2 == 8:
                                                break
                                            if num2 == 9:
                                                print("Gracias por volar con nosotros")
                                                bucle1 += 1
                                                break
    if num == 4:
        bucle2 += num
        while bucle2 == 14:
            print("Oprima 1 si necesita sobrepeso")
            print("Oprima 2 si necesita maleta extra")
            num3 = int(input("> "))
            if num3 == 1:
                cantidad_sobrepeso = int(input("Favor ingrese la cantidad de maletas en las que desea sobrepeso "))
                if cantidad_sobrepeso > 3:
                    print("El número máximo de maletas con sobrepeso aceptadas son 3")
                    print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                else:
                    print(categorias)
                    categoria = input("Escriba la categoría a la que desea exederse ")
                    if categoria not in categorias:
                        print("Categoría no valida")
                        print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                        num2 = int(input("> "))
                        if num2 == 8:
                            break
                        if num2 == 9:
                            print("Gracias por volar con nosotros")
                            bucle1 += 1
                            break
                    else:
                        sobrepeso = random.randint(10000, 99999)
                        print(str(cantidad_sobrepeso) + " maletas han sido ajustadas a " + categoria + " de sobrepeso")
                        print("Su número de transacción es " + str(sobrepeso))
                        print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                        num2 = int(input("> "))
                        if num2 == 8:
                            break
                        if num2 == 9:
                            print("Gracias por volar con nosotros")
                            bucle1 += 1
                            break
            if num3 == 2:
                print(maletas)
                maleta = input("Escriba la maleta a seleccionar ")
                if maleta not in maletas:
                    print("Maleta no valida")
                    print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                else:
                    cantidad_extra = int(input("Escriba la cantidad de maletas a seleccionar "))
                    if cantidad_extra > 7:
                        print("La cantidad máxima de maletas extras a seleccionar son 7")
                        print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                        num2 = int(input("> "))
                        if num2 == 8:
                            break
                        if num2 == 9:
                            print("Gracias por volar con nosotros")
                            bucle1 += 1
                            break
                    else:
                        print(str(cantidad_extra) + " maletas extras de " + maleta + " han sido añadidas")
                        extra = random.randint(10000, 99999)
                        print("Su número de transacción es " + str(extra))
                        print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                        num2 = int(input("> "))
                        if num2 == 8:
                            break
                        if num2 == 9:
                            print("Gracias por volar con nosotros")
                            bucle1 += 1
                            break
    if num == 5:
        bucle2 += num
        while bucle2 == 15:
            boleto = input ("Favor ingrese número de boleto ")
            NIT = input("Favor ingresar NIT ")
            if len(NIT) != 17:
                print("El número de NIT es incorrecto, debe tener 17 caracteres según ejemplo: 0000-000000-000-0")
                print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                num2 = int(input("> "))
                if num2 == 8:
                    break
                if num2 == 9:
                    print("Gracias por volar con nosotros")
                    bucle1 += 1
                    break
            else:
                NRC = input("Favor ingrese NRC ")
                if len(NRC) != 8:
                    print("El número de NRC es incorrecto, debe tener 8 caracteres según ejemplo: 000000-0")
                    print("Oprima 0 para volver a empezar, 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                else:
                    correo = input("Favor ingrese su correo electronico ")
                    arroba = "@"
                    punto = "."
                    if arroba and punto not in correo:
                        print("El correo electronico introducido no existe")
                        print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                        num5 = int(input("> "))
                        if num5 == 8:
                            break
                        if num5 == 9:
                            bucle1 += 1
                            print("Gracias por volar con nosotros")
                            break
                    else:
                        print("Se ha enviado un crédito fiscal al correo " + correo + " para el número de boleto " + boleto)
                        print("Oprima 8 para volver al menu principal o 9 para salir de la llamada")
                        num2 = int(input("> "))
                        if num2 == 8:
                            break
                        if num2 == 9:
                            print("Gracias por volar con nosotros")
                            bucle1 += 1
                            break
    if num == 6:
        bucle2 += num
        while bucle2 == 16:
            print("Oprima 1 si es un reclamo economico")
            print("Oprima 2 si es un reclamo de atención al cliente")
            num4 = int(input("> "))
            if num4 == 1:
                boleto = input("Favor ingrese su número de boleto ")
                motivo = input("Favor ingrese una breve descripción del reclamo ")
                print(monedas)
                moneda = input("Favor ingrese la moneda en la que esta expresada el monto ")
                moneda = moneda.capitalize()
                monto = float(input("Favor ingrese el monto que esta reclamando "))
                if moneda == "Colones":
                    conversion = monto / 8.75
                    reclamo = random.randint(10000, 99999)
                    print("El reclamo por el valor de " + str(round(conversion,2)) + " dolares americanos, en relacion al número de boleto " + boleto + " ha sido introducido")
                    print("Su número de reclamo es " + str(reclamo))
                    print("Oprima 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                elif moneda == "Quetzales":
                    conversion = monto / 7.21
                    reclamo = random.randint(10000, 99999)
                    print("El reclamo por el valor de " + str(round(conversion,2)) + " dolares americanos, en relacion al número de boleto " + boleto + " ha sido introducido")
                    print("Su número de reclamo es " + str(reclamo))
                    print("Oprima 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                elif moneda == "Pesos":
                    conversion = monto / 20
                    reclamo = random.randint(10000, 99999)
                    print("El reclamo por el valor de " + str(round(conversion,2)) + " dolares americanos, en relacion al número de boleto " + boleto + " ha sido introducido")
                    print("Su número de reclamo es " + str(reclamo))
                    print("Oprima 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                elif moneda == "Dolares":
                    conversion = monto / 1
                    reclamo = random.randint(10000, 99999)
                    print("El reclamo por el valor de " + str(round(conversion,2)) + " dolares americanos, en relacion al número de boleto " + boleto + " ha sido introducido")
                    print("Su número de reclamo es " + str(reclamo))
                    print("Oprima 0 para volver al sub-menu 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                else:
                    print("La moneda utilizada no esta disponible en nuestro sistema")
                    print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
            elif num4 == 2:
                print(medios)
                medio = input("Escriba el medio por el cual se dio el incidente: ")
                medio = medio.capitalize()
                if medio not in medios:
                    print("Medio ingresado no es válido")
                    print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                    num2 = int(input("> "))
                    if num2 == 8:
                        break
                    if num2 == 9:
                        print("Gracias por volar con nosotros")
                        bucle1 += 1
                        break
                else:
                    if medio == "Counter":
                        print(origenes)
                        terminal = input("Escriba la terminal en la que se dio el incidente ")
                        terminal = terminal.capitalize()
                    fecha_incidente = input("ingrese la fecha del incidente en formato mm/dd/aaaa ")
                    posicion2_incidente = fecha_incidente[2]
                    posicion5_incidente = fecha_incidente[5]
                    posicion9_incidente = fecha_incidente[6:10]
                    año_actual = int(time.strftime("%Y"))
                    if posicion2_incidente and posicion5_incidente != "/":
                        print("la fecha del incidente es erronea o no cumple el formato")
                        print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                        num2 = int(input("> "))
                        if num2 == 8:
                            break
                        if num2 == 9:
                            print("Gracias por volar con nosotros")
                            bucle1 += 1
                            break
                    elif int(posicion9_incidente) < año_actual - 2:
                        print("la fecha del incidente ya no es válida")
                        print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                        num2 = int(input("> "))
                        if num2 == 8:
                            break
                        if num2 == 9:
                            print("Gracias por volar con nosotros")
                            bucle1 += 1
                            break
                    else:
                        mes_incidente = int(fecha_incidente[0:2])
                        dia_incidente = int(fecha_incidente[3:5])
                        if mes_incidente > 12 or dia_incidente > 31:
                            print("la fecha de salida es erronea o no cumple el formato")
                            print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                            num2 = int(input("> "))
                            if num2 == 8:
                                break
                            if num2 == 9:
                                print("Gracias por volar con nosotros")
                                bucle1 += 1
                                break
                        else:
                            boleto = input("Favor número de boleto relacionado al incidente ")
                            persona = input("Si conoce el nombre del ejecutivo que lo atendió, favor ingrese el nombre ")
                            motivo = input("Favor ingrese una breve descripción del reclamo ")
                            print("El incidente con el ejecutivo " + persona + ", por medio del " + medio + ", en relacion al número de boleto " + boleto + " ha sido introducido")
                            incidente = random.randint(10000,99999)
                            print("Su número de incidente es el "+ str(incidente))
                            print("Oprima 0 para volver al sub-menu, 8 para volver al menu principal o 9 para salir de la llamada")
                            num2 = int(input("> "))
                            if num2 == 8:
                                break
                            if num2 == 9:
                                print("Gracias por volar con nosotros")
                                bucle1 += 1
                                break
            else:
                print("la opción elegida no es válida")
                print("Oprima 8 para volver al menu principal o 9 para salir de la llamada")
                num2 = int(input("> "))
                if num2 == 8:
                    break
                if num2 == 9:
                    print("Gracias por volar con nosotros")
                    bucle1 += 1
                    break
    if num == 7:
        print("Espere en linea para ser atendido")
        print("Oprima 8 para volver al menu o 9 para salir de la llamada")
        num2 = int(input("> "))
        if num2 == 9:
            print("Gracias por volar con nosotros")
            break
    if num == 8:
        print("")
    if num == 9:
        print("Gracias por volar con nosotros")
        break