# LISTAS

my_list = list()
my_other_list  = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)

print(len(my_list))

my_other_list = [33, 1.83 , "Jonathan", "Sanchez"]
print(my_other_list[1])
print(my_other_list.count(33))
print(type(my_other_list))

my_list.append(22)
my_list.insert(1, 'jona')

my_list.remove("jona")
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(2)
print(my_list)

my_list.sort()
print(my_list)
