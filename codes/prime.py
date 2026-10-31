import math


n1=int(input("Enter the number:"))
count=0

for i in range(1,int(math.sqrt(n1))+1):
    if n1%i== 0 :
        count+=1
        if n1//i !=i :         ## Avoid repeated print of middle factor
            count+=1

print(count)
if count==2:
    print("Prime number")
else:
    print("not Prime")