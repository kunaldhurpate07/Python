


arr=[8,3,1,7,5,4,2]
n=len(arr)

def fun(arr,n,x=1):
    if x==n:
        return
    else:
        ele=arr[x]
        i=x-1
    
    while(i>=0 and arr[i]>ele):
        arr[i+1]=arr[i]
        i-=1
    arr[i+1]=ele
    fun(arr,n,x+1)

fun(arr,len(arr))
print(arr)



# for i in range(1,n,1):
#     ele=arr[i]
#     j=i-1
#     while(j>=0 and arr[j]>ele):
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=ele
# print(arr)