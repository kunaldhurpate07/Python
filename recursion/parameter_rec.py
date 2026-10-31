

n=int(input("Enter the number:"))

def fun(n,sum):
    if n==0:
        print(sum)
        return
    return fun(n-1,sum+n)

fun(n,0)