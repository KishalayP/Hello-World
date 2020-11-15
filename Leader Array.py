x=[int(x) for x in input("Enter multiple value: ").split()]
n=len(x)
print(n)
for i in range(0,n):
    k=0
    c=x[i]
    for j in range(i+1,n):
        if(c>x[j]):
            k=k+1 
    if(k>=((n-1)-i)):
        print(c)