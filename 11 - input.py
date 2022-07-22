#nombre = input("¿Cual es tu nombre? : \r\n")

#print(f"Hola {nombre}")

# Leer datos que seran numeros

edad = input("¿Cual es tu edad? : \r\n")
# Convertir edad string a entero
edad = int(edad)

if edad >=18:
    print("Ya puedes votar")
else:
    print("Aún no puedes votar")
    
# Mezclarlo con operadores
numero = input("Agrega un numero y te dire si es par o impar : \r\n")
numero = int(numero)

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")
    
# RETO
nota = 0
pregunta = input("¿Hoy tome cafe? : \r\n")
pregunta2 = input("¿Hoy trabaje? : \r\n")
pregunta3 = input("¿Trabajo en mexico? : \r\n")

if pregunta == "si":
    nota = nota +1 # ASI SE HACE EL CONTADOR EN PYTHON.
if pregunta2 == "si":
    nota = nota +1
if pregunta3 == "si":
    nota = nota +1
else:
    nota = nota +0
    
print(f"Tu nota es de {nota} puntos")

    


   
    
