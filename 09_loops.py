# LOOPS BUCLES CICLOS #

# while hay que pasarle una condicion
# mientras sea verdadero has algo

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condicion es mayor o igual a 10")

print("la ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break
    
    print(my_condition)

print("La ejecucion continua")

# for
# UN BUCLE FOR NOS SIRVE PARA ITERAR UN LISTADO DE ELEMENTOS

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)