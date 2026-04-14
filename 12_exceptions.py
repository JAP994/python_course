# EXCEPTIONS # MANEJO DE ERRORES

number_one = 5
number_two = 5
number_two = "1"

# CAPTURA DE EXCEPCIONES POR TIPO
try:
    print(number_one + number_two)
    print("No se ha producido el error")
except TypeError as error:
    print("Se ha producido el TypeError", error)
except ValueError as error:
    print("Se ha producido el ValueError", error)