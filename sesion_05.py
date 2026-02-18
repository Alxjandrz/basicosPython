
# PUNTO 3 EJEMPLO __INIT__
class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Crear un objeto
mi_cel = Celular("Apple", "iPhone 15")

print(mi_cel.marca)  # Apple

# PUNTO 5 ENCAPSULAMIENTO Y NIVELES DE ACCESO 
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # atributo privado

    def obtener_nombre(self):
        return self.__nombre
    
# PUNTO 6 HERENCIA
class Animal:
    def hacer_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

# PUNTO 7 POLIMORFISMO
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio ** 2
    
# PUNTO 8 COMPOSICION VS HERENCIA
class Motor:
    def encender(self):
        print("Motor encendido")

class Auto:
    def __init__(self):
        self.motor = Motor()

# PUNTO 9 CONCEPTO ESTADO DE UN OBJETO
class Celular:
    def __init__(self):
        self.bateria = 100

    def usar(self):
        self.bateria -= 10