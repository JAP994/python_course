### STRINGS ###

my_strings = "Mi String"
my_string_other = 'Mi otro String'

print(len(my_strings))
print(len(my_string_other))

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

mi_tab_string = "\teste es un string con tabulacion"
print(mi_tab_string)

# FORMATEANDO CADENAS DE  TEXTO
name, surname, age = "Jonathan", "Alexis", 32
print('mi nombre es {} {} y mi edad es {}'.format(name, surname, age))
print('mi nombre es %s %s y mi edad es %d' %(name, surname, age))

# INFERENCIA DE DATOS
print(f'mi nombre es {name} {surname} y mi edad es {age}')
