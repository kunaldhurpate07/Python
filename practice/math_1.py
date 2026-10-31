import random


x=4
print(type(x))
print(complex(x))

# Round function

a=-44

print(abs(a))

s=44.2
print(round(s))
print(round(44.5))
print(round(45.5))

## Random()- print any random value
print(random.random())

print(isinstance(3,int)) #checks data type

#Check if any value is missing in list

xx=[4,5,6,7]
print(any([4,5," ",7,8,9])) # it uses or operation
print(any(xx))

print(all(xx)) # it uses and operation