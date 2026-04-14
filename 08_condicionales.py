# Conditionals #

# SI SE CUMPLE UNA CONDICION SE EJECUTA LO QU ESTA DENTRO DEL CONDICIONAL

my_condition = True

if my_condition: 
    print("Se ejecuta la condicion del if")

my_condition = 5 * 2

if my_condition == 11:
    print("Se ejecuta la condicion del segundo if")


if my_condition >= 10:
    print("Se ejecuta la condicion del tercer if")

print("La ejecucion continua")


# TENEMOS DIFERENTES CONDICIONALES AQUI SE PUEDEN USAR LOS OPERADORES
# and, or, not, etc.
my_condition = 1
if my_condition  > 10 and my_condition  < 20:
	print("Es mayor que 10 y menor que 20")
elif my_condition  == 1:
	print("es igual a 1")
else:
	print("Es menor o igual que 10 o mayor o igual a 20")