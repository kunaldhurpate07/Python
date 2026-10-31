n=int(input("Enter Num:"))

def num(i,n):
    if n<i:
        return
    print(i)
    num(i+1,n)

num(1,n)