def app():
    # Crear el archivo
    archivo = open("archivo.txt", "w") # w es escritura, si no existe lo creara.
    
    # Generar numeros en archivo
    for i in range(0, 20):
        archivo.write("Esta es la linea " + str(i) +"\r\n") # write es el metodo para escribir en un archivo.
        
    # Cerrar el archivo
    archivo.close()
        

app()