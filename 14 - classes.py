class Restaurant:
    
    def agregar_restaurant(self, nombre):
        self.nombre = nombre # Atributo de la clase, self es una forma de referirse al mismo objeto.
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        

# Instanciar la clase (Primer objeto)
restaurant = Restaurant()
restaurant.agregar_restaurant("Pizzeria mexico")
restaurant.mostrar_informacion()

# Segunda instancia (Segundo objeto)
restaurant2 = Restaurant()
restaurant2.agregar_restaurant("Hamburguesas Python")
restaurant2.mostrar_informacion()

# Mostrar la informacion
print(f"Nombre Restaurant: {restaurant.nombre}")
print(f"Nombre Restaurant: {restaurant2.nombre}")
