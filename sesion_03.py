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