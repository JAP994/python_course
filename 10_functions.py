# Functions #

def my_function():
    print("Esto es una funcion")

my_function()

def sum_two_values(first_value: int, second_value: int):
    print(first_value + second_value)

sum_two_values(2,3)

def sum_two_values_with_return(first_value: int, second_value: int):
    return first_value + second_value

my_result = sum_two_values_with_return(10,5)
print(my_result)
print(type(my_result))

def print_name(name, surname):
    print(f'{name} {surname}')

print_name("Jonathan", "Sanchez")

def print_name(name, surname, alias = "Sin alias"):
    print(f'{name} {surname} {alias}')

print_name("Jonathan", "Sanchez", "Suco")
print_name("Jonathan", "Sanchez")

# IMPRIMIR TODOS LOS TEXTOS EN MATUSCULAS
def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("hola", "python", "mp")