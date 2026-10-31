

arr=[9,2,7,3,8,4,1,6]
n=len(arr)

def fun(arr,a=0):
    if a==n-1:
        return
    min=a
    for j in range(a+1,n):
        if arr[j]<arr[min]:
            min=j
            
    temp=arr[a]
    arr[a]=arr[min]
    arr[min]=temp
    fun(arr,a+1)

fun(arr)

print(arr)