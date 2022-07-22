import os
from pickle import TRUE # Libreria diseñada para manejar archivos

CARPETA = "contactos/" # En mayuscula es porque es una constante, que no se debe modificar el valor de la carpeta (CARPETA DE CONTACTOS)
EXTENSION = ".txt" # Extension de archivos

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
        
        
def app ():
    # Revisa si la carpeta existe o no
    
    crear_directorio()
    
    # Muestra el menu de opciones
    mostrar_menu()
    
    # Preguntar al usuario la accion a realizar
    
    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opcion: \r\n")
        opcion = int(opcion) # Convertir string a numero.
        
        # Ejecutar opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print("Opcion no valida, intente de nuevo")


def eliminar_contacto():
     nombre = input("Seleccione el Contacto que desea eliminar: \r\n")
     
     try:
         os.remove(CARPETA + nombre + EXTENSION)
         print("\r\nEliminado Correctamente")
     except IOError:
         print("No existe ese Contacto")
         print(IOError)
    
     # Reiniciar app
     app()
                     
def buscar_contacto():
    nombre = input("Seleccione el Contacto que desea buscar: \r\n")
    
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print("\r\n Informacion del contacto \r\n")
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")
    except IOError:
        print("El archivo no existe")
        print(IOError)
        
    # Reiniciar la app
    app()
           
def mostrar_contactos():
    archivos = os.listdir(CARPETA) # Nos permite listar los archivos de un directorio
    
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)] # Recorrer el iterador solo si el archivo es .txt
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # Imprime los contedios
                print(linea.rstrip())
            # Imprime un separador entre contactos    
            print("\r\n")
           
def editar_contacto():
    print("Escribe el nombre del contacto a editar")
    nombre_anterior = input("Nombre del contacto que desea editar:\r\n")
    
    #Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)
    
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, "w" ) as archivo:
            
            # Resto de los campos
            nombre_contacto = input("Agrega el Nuevo Nombre:\r\n")
            telefono_contacto = input("Agrega el Nuevo Telefono:\r\n")
            categoria_contacto = input("Agrega la Nueva Categoria:\r\n")
            
            # Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            # Escribir en el archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Telefono: " + contacto.telefono + "\r\n")
            archivo.write("Categoria: " + contacto.categoria + "\r\n")
            
            # Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
            
            # Mostrar un mensaje de exito
        print("\r\n Contacto Editado correctamente \r\n")
            
    else:
        print("Ese Contacto no existe")
        
    # Reiniciar la aplicacion
    app()
    
def agregar_contacto():
    print("Escribe los datos para agregar el nuevo Contacto")
    nombre_contacto = input("Nombre del Contacto:\r\n")
    
    #Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto) #nombre_anterior? o nombre_contacto?
    
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, "w" ) as archivo: # Tiene la ventaja de que no es necesario tener que cerrar el archivo
        
            # Resto de los campos
            telefono_contacto = input("Agrega el Telefono:\r\n")
            categoria_contacto = input("Categoria Contacto:\r\n")
        
            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
        
            # Escribir en el archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Telefono: " + contacto.telefono + "\r\n")
            archivo.write("Categoria: " + contacto.categoria + "\r\n")
        
            # Mostrar un mensaje de exito
            print("\r\n Contacto creado correctamente \r\n")
            
    else:
        print("Ese Contacto ya existe")
        
    # Reiniciar la app
    app()
                              
def mostrar_menu():
    print("Seleccione del menu lo que desea hacer:")
    print("1) Agregar Nuevo Contacto")
    print("2) Editar Contacto")
    print("3) Ver Contactos")
    print("4) Buscar Contacto")
    print("5) Eliminar Contacto")
    
def crear_directorio():
    if not os.path.exists(CARPETA):
        # Si esta capreta no existe, entonces crear la carpeta
        os.makedirs(CARPETA) # Crea la carpeta

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION) # Va a revisar si el archivo ya existe previamente
    
          
app()
