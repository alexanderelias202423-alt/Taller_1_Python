import os
import time

def celsius_a_fahrenheit(celsius):
    return(celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return(fahrenheit -32) * 5/9

flag = True
while flag:
    print("--Bienvedino a esta calculadora--")
    print("--Menu--")
    print("1) celsius_a_fahrenheit ")
    print("2) fahrenheit_a_celsius ")
    print("0) salir")
    print("--------------------------------------")
    opc= input("Ingrese una opcion: ")
    os.system("cls")

    match opc:
        case"1":
            grados = float(input("Ingrese en celsius: "))
            resultado = celsius_a_fahrenheit(grados)
            print(f"{grados} celsius equivale a {resultado}")
            os.system("pause")
        case"2":
            grados = float(input("Ingrese en fahrenheit: "))
            resultado = fahrenheit_a_celsius(grados)
            print(f"{grados} fahrenheit equivale a {resultado}")
            os.system("pause")
        case"0":
            flag = False
            print("Hasta luego")
            time.sleep(3)
            os.system("cls")