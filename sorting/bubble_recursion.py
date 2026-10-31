
arr=[2,3,4,5,6,9,7]
a=len(arr)
def fun(arr,n):
    s=0
    for j in range(n-1):
        if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                    x=1
        if x==0:
            return
        fun(arr,n-1)

print(arr)