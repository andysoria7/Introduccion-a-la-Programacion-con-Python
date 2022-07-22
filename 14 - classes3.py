# Encapsulamiento

class Restaurant:
    
    def __init__(self, nombre, categoria, precio): # Constructor
        self.nombre = nombre # Atributo de la clase, "self" es una forma de referirse al mismo objeto.
        self.categoria = categoria
        self.__precio = precio # Default: Public, _PROTECTED, __PRIVATE
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}")
        
    # GETTERS Y SETTERS - GET = OBTIENE UN VALOR, SET = AGREGA UN VALOR
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio
        
    

# Instanciar la clase (Primer objeto)
restaurant = Restaurant("Pizzeria mexico", "Comida Italiana", 50)
# restaurant.__precio = 80 # No sera posible modificarlo por PRIVATE __
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_precio()
print(precio)


# Segunda instancia (Segundo objeto)
restaurant2 = Restaurant("Hamburguesas Python", "Comida Casual", 20)
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
precio = restaurant2.get_precio()
print(precio)