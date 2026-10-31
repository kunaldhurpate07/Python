import math

arr=[1,2,3,4,5,6]

print(max(arr))
c=0
max=arr[0]
for i in range(1,len(arr)):
    if max< arr[i]:
        max=arr[i]
        c+=1

print(max)
print(c)