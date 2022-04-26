""""
Date:       2022-04-13
Authors:    Jorge de Jesus Hernandez Rivera
File:       T1E1_pos_neg.py
Brief:      Programa que obtiene un numero entero o flotante y determina
            si es positivo,negativo o cero.   
Version:    1.1.1
Fixes:      

Recomendaciones a seguir con PEP8

            - PEP8 recomienda añadir un espacio en blanco después del
                carácter de almohadilla '#' de los comentarios

            - PEP8 recomienda añadir espacios en blanco alrededor de
                los operadores
"""

print("Programa que obtiene un numero entero o flotante y determina si es positvo,negativo o cero \n") # PEP8

#Metodo de validacion                                       

while True:                                                
    try:
        a = float(input("Valor de numero: "))               
        if a > 0:
            print("El numero: "+str(a)+" es positivo")      
            break
        elif a < 0:
            print("El numero: " + str(a) + " es negativo")
            break
        else:
            print("El numero: " + str(a) + " es cero")
            break

    except ValueError:                                      
        print('Error,introduce un numero')
