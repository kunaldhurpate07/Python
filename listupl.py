my_list = [1, 2, 3, 4, 5]
my_tuple = (1,2,3,4,5)

print(my_list)
print(my_tuple)
print(type(my_list))
print(type(my_tuple))


tuple_list = list(my_tuple)
tuple_list[0] = 7
print(tuple_list)
print(type(tuple_list))

my_tuple = tuple(tuple_list)
print(my_tuple)