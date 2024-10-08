def switch_case(option):
    if option == 1:
        numero_1 = int(input('Ingresar el primer numero: '))
        numero_2 = int(input('Ingresar el segundo numero: '))
        print('Punto A: ',numero_1 + numero_2)
    elif option == 2:
        numero_1 = int(input('Ingresar el primer numero: '))
        numero_2 = int(input('Ingresar el segundo numero: '))
        print('Punto B: ',numero_1 * numero_2)
    elif option == 3:
        numero_1 = int(input('Ingresar el primer numero: '))
        numero_2 = int(input('Ingresar el segundo numero: '))
        print('Punto C: ', str(numero_1),'', str(numero_2))
    elif option == 4:
        import math
        radio = int(input('Ingresar el radio: '))
        area = math.pi * radio ** 2
        print('El area del circulo es', area)  
        """INFO: Para elevar un numero ** y luego el numero"""  
    elif option == 5:
        base = float(input('Ingrese la base del rectangulo: '))
        altura = float(input('Ingrese la altura del rectangulo: '))
        area = base * altura
        print('El area del rectangulo es', area)
    elif option == 6:
        texto1 = 'Soy'
        texto1 += ' '
        texto2 = 'Carlos'
        texto2 += 'Javier Mahecha Gomez'
        unirmensajes = texto1 + ' ' + texto2
        print('Primer forma del texto  concatenado es:',texto1)
        print('Primer forma del texto  concatenado es:',unirmensajes)
        print('Invertir cadena de texto:',unirmensajes[::-1])
        print('Longitud del texto sin invertir: ',len(unirmensajes))
    elif option == 7:
        lista= [2,2,2,2]
        print('Lista',lista)
        print('Promedio de una lista de numeros:',sum(lista)/len(lista))
    else:
        return "Opcion no válida"
 
print('1. Suma')
print('2. Multiplicacion')
print('3. Convertir los dos numeros enteros a cadena pero antes indicando que tipo de variable es')
print('4. Calcular el area de un circulo con un radio dado')
print('5. Calcular el area de un rectangulo pide la base y altura al usuario')
print('6. Concatenar dos cadenas de texto, luego invertir el texto y decir su longitud')   
print('7. Crear lista y calcular el promedio de una lista de numeros e imprimir resultados')
opcion = int(input("Selecciona una opción: "))
switch_case(opcion)