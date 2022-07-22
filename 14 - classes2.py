#Abstraccion y constructores

class Restaurant:
    
    def __init__(self, nombre, categoria, precio): # Constructor
        self.nombre = nombre # Atributo de la clase, self es una forma de referirse al mismo objeto.
        self.categoria = categoria
        self.precio = precio
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}")

# Instanciar la clase (Primer objeto)
restaurant = Restaurant("Pizzeria mexico", "Comida Italiana", 50)
restaurant.mostrar_informacion()


# Segunda instancia (Segundo objeto)
restaurant2 = Restaurant("Hamburguesas Python", "Comida Casual", 20)
restaurant2.mostrar_informacion()
