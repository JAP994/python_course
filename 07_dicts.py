# Diccionario de datos PYTHON

my_dict = dict()
my_other_dict = dict()

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Jona", "Apellido":"Sanchez","Edad":32, 1:"Python"}
my_dict = {
    "Nombre":"Jona",
    "Apellido":"Sanchez",
    "Edad":32,
    "Languages":{"Python","Swift", "Kotlin"},
    1:"1.77"
}

print(my_dict)
print(my_other_dict)

# AGREGAR UN NUEVO DATO A UN DICCIONARIO
my_dict["Calle"] = "Calle ARMI"
print(my_dict)
print(my_dict["Languages"])

# ELIMINAR DATOS O ELEMENTOS DE UN DICCIONARIO
del my_dict["Languages"]
print(my_dict)
print(my_dict.values())