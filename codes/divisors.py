import math


# n=int(input("Enter the number:"))

# for i in range(1,n+1):
#     if n%i== 0 :
#         print(i)

# # more optimized:

n1=int(input("Enter the number:"))


for i in range(1,int(math.sqrt(n1))+1):
    if n1%i== 0 :
        print(i)
        if n1//i !=i :         ## Avoid repeated print of middle factor
            print(n1//i)