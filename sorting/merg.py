
arr=[13,46,24,52,20,9]

def fun(arr,s,e):
    if(s<e):
        m=(s+e)//2
        fun(arr,s,m)
        fun(arr,m+1,e)
        merge(arr,s,m,e)

def merge(arr,s,m,e):
    n1=m-s+1
    n2=e-m

    arr1=[0]*n1
    arr2=[0]*n2

    for i in range(0,n1):
        arr1[i]=arr[s+i]

    for j in range(n2):
        arr2[j] = arr[m+1+j]

    i,j,k=0,0,s
 
    ## Insert all elements in i array and j array in k array
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            arr[k] = arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]
            j+=1
        k+=1

    while(i<n1):
        arr[k] = arr1[i]
        i+=1
        k+=1

    while(j<n2):
        arr[k] = arr2[j]
        j+=1
        k+=1

fun(arr,0,len(arr)-1)
print(arr)