import math

arr=[1,2,3,4,5,6]

# arr1=arr.sort()

# for i in range(len(arr)-1, -1, -1):
#     if arr[i] < arr[-1]:
#         print(arr[i])
#         break

max1=arr[0]
for i in range(1,len(arr)):
    if max1< arr[i]:
        max1=arr[i]

max2=0
for j in range(len(arr)):
    if arr[j]>max2 and arr[j]!=max1:
        max2=arr[j]

print(max2)