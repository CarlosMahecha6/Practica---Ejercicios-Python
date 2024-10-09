import sys
import os
import math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos')))

"""Declaramos funciones a utilizar"""
def saludar(nombre):
    print("Hola ",nombre)  

def saludar2(nombreDigitado):
    print("Hola! ",nombreDigitado)
    
def suma(num1, num2, multi):
    suma = num1 + num2
    print(suma)
    return multiplicacion(suma, multi)

def multiplicacion(opSuma, multplicador):
    mult = opSuma * multplicador
    print(mult)
  
"""Creacion del Switch Case"""  
def swichtCaseFunciones(options):
    if options == 1:
        saludar("Carlos Mahecha")   
    elif options == 2:
        nombreDigitado = (input("Digite su nombre: "))
        saludar2(nombreDigitado)
    elif options ==3:
        numero1 = int(input("Digite numero 1: "))
        numero2 = int(input("Digite numero 2: "))
        multiplicador = int(input("Digite multiplicador: "))
        suma(numero1,numero2, multiplicador)
    elif options ==4:
        import datos
        datos = datos.bibiografia()
        print(datos)
    elif options ==5:
        import datos
        nombre = (input("Digite su nombre: "))
        ano_nacimiento = int(input("Digite su año de nacimiento: "))
        datos = datos.infos_datos_enviados(nombre,ano_nacimiento)
        print(datos)
    elif options ==6:
        import estudiantes
        def promedio():
            notas_utilizar = estudiantes.registro()
            notas = [estudiante['Nota'] for estudiante in notas_utilizar]
            if len(notas) == 0:
                return None
            suma_total = math.fsum(notas,)
            promedio = suma_total / len(notas) 
            return promedio
        
        promedioFinal = promedio()
        print(promedioFinal)
    else:
        return "No valido"
    
"""Declaramos el Menu"""
print("1. Ver tu nombre ya definido")
print("2. Ver tu nombre digitado")
print("3. Realizar suma de dos numeros y hacer multiplicacion del resultadi con otro numero en diferentes funciones")
print("4. Traer info de otro archivo que se encuentra en otra carpeta (Modulo)")
print("5. Traer una funcion que se encuentra en otra carpeta para que opere con los datos que le enviamos por consola (Modulo)")
print("6. Traer una notas y sacar promedio (Modulo)")
opcions = int(input("Selecciona una opción: "))
swichtCaseFunciones(opcions)