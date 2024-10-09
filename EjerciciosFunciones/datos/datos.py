def bibiografia():
    data = "Mi nombre es Carlos Mahecha Gómez, teng 21 años y naci en el municipio de Palermo - Huila."
    return data

def infos_datos_enviados(nombre, ano_nacimiento):
    edad = 2024 - ano_nacimiento
    text = "Info final: Nombre: " + nombre + ", Edad: " + str(edad)
    return text