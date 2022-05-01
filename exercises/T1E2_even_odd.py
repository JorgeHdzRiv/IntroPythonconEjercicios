""""
Date:       2022-04-29
Authors:    Jorge de Jesus Hernandez Rivera
File:       T1E2_even_odd.py
Brief:      Programa que determina si un numero entero es par o impar
Score:      110
Version:    1.1.1
Fixes:     
"""

print("Programa que determina si un numero entero es par o impar")

#Metodo Validacion          

while True:
    try:
        a = int(input("Valor de numero entero: "))

        if a % 2 == 0:
            print("El numero: " + str(a) + " es par")
            break
        else:
            print("El numero: " + str(a) + " es impar")
            break
     
    except ValueError:
        print('Error,digite un numero entero')
