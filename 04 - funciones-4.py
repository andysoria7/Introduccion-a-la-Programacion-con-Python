# Diferencia entre funciones y metodos

# Funcion

nombre = "andres"
def mostrar_nombre(nombre):
    print(f" Hola {nombre}")

mostrar_nombre(nombre)

# Metodo

print( nombre.upper() )
print( nombre.title() )

#Reto : Crear una funcion que imprima un mensaje de bienvenida

def mensaje_bienvenida():
    print("Bienvenido!!!")
mensaje_bienvenida()

# Crea una funcion que tome un nombre de usuario y lo muestre como mensaje debienvenida

nombre_usuario = "Marcelo"
def mostrar_mensaje_bienvenida_usuario(nombre_usuario):
    print(f"Bienvenido {nombre_usuario}")

mostrar_mensaje_bienvenida_usuario(nombre_usuario)

# Crea una funcion que tome la ultima actividad que hiciste

def actividad(actividad):
    return actividad

ultima_actividad = actividad("Futbol")
print(ultima_actividad)