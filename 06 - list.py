from operator import le


lenguajes = ["Python", "Kotlin", "Java", "Javascript"]
print(lenguajes)

# Los arrays list comienzan en la posicion 0
print(lenguajes[0]) # Python

# Ordenar los elementos
lenguajes.sort() #Ordena los elementos alfabeticamente
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f"Estoy aprendiendo {lenguajes[3]}"

print(aprendiendo)

# Modificando valores de un arreglo (list)
lenguajes[2] = "PHP"
print(lenguajes)

# Agregar elementos a un arreglo (list)
lenguajes.append("RUBY") # append() es para agregar un elemento de cualquier tipo al final de una lista.
print(lenguajes)

# Eliminar de un arreglo (list)
del lenguajes[1]
print(lenguajes)

# Eliminar de un arreglo (list)
lenguajes.pop() # Elimina el ultimo elemento
print(lenguajes)

# Eliminar con pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

# Eliminar por nombre

lenguajes.remove("PHP")
print(lenguajes)

