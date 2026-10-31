# arr=[]

# n=int(input("Enter the number of elements in the array: "))

# for i in range(n):
#     x=int(input("Enter element: "))
#     arr.append(x)
# arr=[7,3,9,4,2,5,6]
arr=[2,3,4,5,6,9,7]
n=len(arr)
print("The original array is:", arr)


for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        

print(c)
print(arr)