
print("--Bienvedino a esta calculadora--")
print("--Menu--")
print("1) Suma ")
print("2) Resta ")
print("3) Multi ")
print("4) Div ")
print("--------------")

opc = input("Ingresa la opcion que quieres:")

match(opc):
    case "1":
        a =float(input ("Ingrese un numero: "))
        b = float(input("Ingresa un numero: "))
        sum = a + b
        print(f"{a} + {b} = {sum}")

    case "2":
        a =float(input ("Ingrese un numero: "))
        b = float(input("Ingresa un numero: "))
        resta = a - b
        print(f"{a} - {b} = {resta}")

    case "3":
        a =float(input ("Ingrese un numero: "))
        b = float(input("Ingresa un numero: "))
        mult = a * b
        print(f"{a} * {b} = {mult}")
          
    case "4":
        a =float(input ("Ingrese un numero: "))
        b = float(input("Ingresa un numero: "))
        if a == 0 or b == 0:
            print("No se puede realizar esta division")
        else:
            div = a / b
            print(f"{a} / {b} = {div}")
        