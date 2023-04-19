# 1. Crear una clase `Lapiz` que tenga los atributos `color` (cadena de caracteres) y `grosor` (entero). El constructor debe inicializar ambos atributos con valores por defecto. Agregar un método `escribir` que imprima por pantalla la frase "Escribiendo con un lapiz de [color] y grosor [grosor]". Crear un objeto de la clase `Lapiz` e invocar el método `escribir`.
class Lapiz:
    def __init__(self, color='negro', grosor=1):
        self.color = color
        self.grosor = grosor
    
    def __escribir(self):
        print(f"Un lapiz de {self.color} y grosor {self.grosor}")

    def escribirColor(self):
        self.__escribir()

miLapiz = Lapiz(color='azul', grosor=2)
miLapiz.escribirColor()

# 2. Crear una clase `Flor` que tenga los atributos `nombre` (cadena de caracteres) y `color` (cadena de caracteres). 
# El constructor debe recibir ambos atributos como argumentos e inicializarlos. 
# Agregar un método `mostrar_informacion` que imprima por pantalla el nombre y color de la flor. 
# Crear dos objetos de la clase `Flor` e invocar el método `mostrar_informacion` para ambos.
class Flor:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def mostrarInformacion(self):
        print(f"La flor se llama {self.nombre} y su color es {self.color}")

flor1 = Flor(color='Rojo', nombre='Rosa')
# flor1 = Flor('Rosa', 'Rojo')
flor1.mostrarInformacion()

flor2 = Flor(nombre='Margarita', color='Blanco')
flor2.mostrarInformacion()

# 3. Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de productos.
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Stock: {self.stock}"
    
productosLista = [
    {"nombre": "Leche", "precio": 2.50, "stock": 10},
    {"nombre": "Huevos", "precio": 1.50, "stock": 20},
    {"nombre": "Pan", "precio": 1.00, "stock": 15}
]

listaProductos = []
for producto in productosLista:
    p = Producto(producto['nombre'], producto['precio'], producto['stock'])
    listaProductos.append(p)

for producto in listaProductos:
    print(producto)

# 4. Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de alumnos.
    # La clase deberá tener un método que incorpore el promedio de las notas del alumno.

class Alumno:
    def __init__(self, nombre, apellido, edad, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.notas = notas
        self.promedio = sum(self.notas) / len(self.notas)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Promedio de notas: {self.promedio}"
    
alumnosLista = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "notas": [7, 8, 9]},
    {"nombre": "María", "apellido": "González", "edad": 22, "notas": [6, 9, 10]},
    {"nombre": "Pedro", "apellido": "García", "edad": 21, "notas": [5, 7, 8]}
]

listaAlumnos = []
for alumno in alumnosLista:
    a = Alumno(alumno['nombre'], alumno['apellido'], alumno['edad'], alumno['notas'])
    listaAlumnos.append(a)

for alumno in listaAlumnos:
    print(alumno)
    