# Funciones con parametros y argumentos

def informacion(nombre, puesto = "Desconocido"): #Parametro por default
    print(f"Soy {nombre} y soy {puesto}") # Cuando mezclas un string con variables, debes agregarle al inicio "f"

informacion("Andres", "Programador")
informacion("Marcelo", "Futbolista")
informacion("Soria", "Jugador de padel")