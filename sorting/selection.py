# # arr=[9,2,7,3,8,4,1,6,10]

arr=[13,46,24,52,20,9,]
n=len(arr)

for i in range(0,n-1):
    min = i
    for j in range(i+1,n):
        if arr[j]< arr[min]:
            min = j
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp

print(arr)