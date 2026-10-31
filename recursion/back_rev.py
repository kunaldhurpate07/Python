n=int(input("Enter Num:"))

def back_rev(i,n):
    if i>n:
        return
    back_rev(i+1,n)
    print(i)

back_rev(1,n)