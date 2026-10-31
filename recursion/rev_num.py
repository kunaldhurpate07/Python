n=int(input("Enter Num:"))

def rev_num(n):
    if n==0:
        return
    print(n)
    rev_num(n-1)

rev_num(n)