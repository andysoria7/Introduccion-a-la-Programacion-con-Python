# Operadores and y or
usuario_logueado = True
usuario_admin = True

if usuario_logueado or usuario_admin:
    print("ADMINISTRADOR")
elif usuario_logueado:
    print("ACCESO AL SISTEMA")

else:
    print("DEBES INICIAR SESION")