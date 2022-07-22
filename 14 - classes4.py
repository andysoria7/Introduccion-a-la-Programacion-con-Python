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
        

# Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio) #Super() hace referencia a la clase padre.
        
hotel = Hotel("Hotel POO", "5 ESTRELLAS", 200)
hotel.mostrar_informacion()