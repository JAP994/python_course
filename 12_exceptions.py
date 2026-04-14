# EXCEPTIONS # MANEJO DE ERRORES

number_one = 5
number_two = 5
number_two = "1"

# CAPTURA DE EXCEPCIONES POR TIPO
try:
    print(number_one + number_two)
    print("No se ha producido el error")
except Exception as error:
    print("Se ha producido el TypeError", error)
    