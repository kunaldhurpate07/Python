
n=int(input("Enter the number:"))

def fun(n,rev=0):
    if n==0:
        return rev
    return fun(n//10,rev*10+n%10)

fun(n)
print(fun(n))

if n==fun(n):
    print("Palindrome")
else: 
    print("Not Palindrome")
