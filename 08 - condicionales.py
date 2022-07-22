# Revisar si una condicion es mayor a
balance = 500
if balance > 0:
    print("Puedes pagar")
else:
    print("No tiene saldo")
    
# Likes
likes = 200
if likes >= 200:
    print("Excelenete, 200 likes")
else:
    print("Casi llegas a los 200 likes")
    
# IF con texto
lenguaje = "PHP"
if not lenguaje == "Python": # Estamos evaluando que sea verdadera pero con el not la estamos negando nos trae el valor contrario
    print("Excelente decision")
    
# Evaluar un boolean
usuario_autenticado = True
if usuario_autenticado:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")
    
# Evaluar un elemento de una lista
lenguajes = ["Python", "Kotlin", "Java", "Javascript", "PHP"]
if "PHP" in lenguajes:
    print("PHP si existe")
else:
    print("No, no est en la lista")

# IF anidados
usuario_autenticado = False
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print("ACCESO TOTAL")
    else:
        print("Acceso al sistema") 
else:
    print("Debes iniciar sesion")
