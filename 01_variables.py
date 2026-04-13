# Variables

my_string_variable = "My string variables"
print(my_string_variable)

my_int_variable = 5
my_bool_variable = True
print(my_bool_variable, my_string_variable, my_int_variable, "concatenacion")
# ALGUNAS FUNCIONES DEL SISTEMA
# len cuenta el numero de caracteres de cada string contando
# los espacios
print(len(my_string_variable))

first_name = 'Asabeneh' 
# Printing out types
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip
second_name = input('What is your name:')
age = input('Wow old are you:')
print("nombre; ", second_name, "edad:",  age) 

# De esta forma forzmos el tipo de dato
address: str = 'Mi direccion'
address = 32
print(address)




