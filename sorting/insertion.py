

arr=[8,3,1,7,5,4,2]
n=len(arr)

for i in range(1,n,1):
    ele=arr[i]
    j=i-1
    while(j>=0 and arr[j]>ele):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=ele
print(arr)