from Enemigo import * 

class Zombie(Enemigo):
    def __init__(self, puntos_energia=10, ataque=1):
        super().__init__(tipo_enemigo='Zombie', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("Hummmmm")

    def propagar_enfermedad(self):
        print("El zombie esta tratando de propagar la enfermedad!!")
