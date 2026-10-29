n=int(input("Enter Num:"))

def back(n):
    if n==0:
        return
    back(n-1)
    print(n)

back(n)