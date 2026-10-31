
arr=[3,4,5,6,2,3,4]
n=len(arr)

for i in range(n-1,0,-1):
    ele=arr[i]
    j=i-1
    while(j>=0 and arr[j]>ele):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=ele
print(arr)