#### BOOTCAMP CODING DOJO - Introducción a Python / Hola mundo (Core)
#### ALUMNO: DANTE MARENGO

# 1. Imprime "Hola, mundo"

print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Valeria"

print("Hola,", nombre) # con una coma

print("Hola, " + nombre)  # con un +

# 3. Imprimir "Hola 156!" con el número en una variable

numero = 156

print("Hola", numero, "!") # con una coma

print("Hola " + str(numero) + "!") # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "tacos"

comida2 = "arepas"

print("Me encanta comer {} y {}".format(comida1, comida2)) # con .format()

print(f"Me encanta comer {comida1} y {comida2}")  # con una cadena f

#### Bonus NINJA :)

palabras = ["hola", "Dante MARENGO"]
print(" ".join(palabras))  # usando join()

datos = {"nombre": "Dante MARENGO", "comida1": "Asado Paraguayo", "comida2": "Empanadas"}
print("me encanta comer {comida1} y {comida2}".format_map(datos)) # usando format_map()

print("hola! " * 3) # repitiendo las strings

print("hola, {nombre}. me encanta comer {comida1} y {comida2}.".format(nombre=nombre, comida1=comida1, comida2=comida2)) # usando "format()" con nombres de variables

print("hola, %s!" % nombre) # usando el estilo antiguo con %
print("hola %d!" % numero)






#   (\(\
#   ( -.-)
#    o_(")(")