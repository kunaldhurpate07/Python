
arr=[13,46,24,52,20,9,]
n=len(arr)

for i in range(1,n):
    ele = arr[i]
    j=i-1
    while(j>=0 and arr[j]>ele):
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = ele
print(arr)