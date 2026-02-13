# Loops 

mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("Mi numero es:", i)

    resultado = 0
    for i in mi_lista:
        resultado += i

    print("El resultado de la suma de la lista es:", (resultado)) 
    for i in range(2, 9):
        print(i)

    mi_lista_2 = ["lunes, martes, miercoles, jueves, viernes"]

    for i in mi_lista_2:
        if i == "Lunes":
            print("Feliz", (i))

    # Practica 2 
    # Dada la lista mi_lista_2 = ["lunes, martes, miercoles, jueves, viernes"]
    # Imprimir cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas 
    # Pista: Usalo los dos tipos loop while y for en el mismo programa para lograrlo
    # Resultado: 
    # martes
    # miercoles
    # jueves 
    # viernes
    # martes
    # miercoles
    # jueves 
    # viernes
    # martes
    # miercoles
    # jueves 
    # viernes

    mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

i = 0

while i < 3:
    for dia in mi_lista_2:
        if dia != "lunes":
            print(dia)
    i += 1
