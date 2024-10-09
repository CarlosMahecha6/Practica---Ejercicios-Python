import sys
import os
import math
import pandas as pd #pip install pandas y python.exe -m pip install --upgrade pip
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos')))

#Declaramos funciones a utilizar
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
    
def leer_datos_csv(ruta_archivo):
    try:
        # Leer el archivo CSV
        df = pd.read_csv(ruta_archivo)
        return df
    except Exception as e:
        print("Error al leer el archivo:", e)
        return None

def mostrar_datos():
    ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'datos', 'Departamentos_y_municipios_de_Colombia.csv')
    datos_csv = leer_datos_csv(ruta_csv)
    if datos_csv is not None:
        print("Datos de estudiantes:")
        print(datos_csv)
    else:
        print("No se pudieron cargar los datos.")
        
#Creacion del Switch Case
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
    elif opcions == 7:
        mostrar_datos()
    else:
        return "No valido"
    
#Declaramos el Menu
print("1. Ver tu nombre ya definido")
print("2. Ver tu nombre digitado")
print("3. Realizar suma de dos numeros y hacer multiplicacion del resultadi con otro numero en diferentes funciones")
print("4. Traer info de otro archivo que se encuentra en otra carpeta (Modulo)")
print("5. Traer una funcion que se encuentra en otra carpeta para que opere con los datos que le enviamos por consola (Modulo)")
print("6. Traer una notas y sacar promedio (Modulo)")
print("7. Traer informarcion de un archivo csv u otro (Modulo)")
opcions = int(input("Selecciona una opción: "))
swichtCaseFunciones(opcions)