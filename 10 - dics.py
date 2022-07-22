# Creando un diccionario simple
cancion = {
    "artista" : "Metallica", # Llave y valor
    "cancion" :  "Enter sadman",
    "lanzamiento" : 1992,
    "likes" : 3000
}
# Acceder a los elementos del diccionario
print(cancion["artista"])
print(cancion["lanzamiento"])

# Mesclar con un string
artista = cancion["artista"]
print(f"Estoy escuchando a {artista}")

print(cancion)

# Agregar nuevos valores
cancion["playlist"] = "Heavy metal"
print(cancion)

# Reemplazar valor existente
cancion["cancion"] = "Seek & Destroy"
print(cancion)

# Eliminar un valor
del cancion["lanzamiento"]
print(cancion)