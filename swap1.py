def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
a=int(input("enter a:"))
b=int(input("enter b:"))
a,b=swap(a,b)
print(f"a={a},b={b}")
