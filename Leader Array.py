x=[int(x) for x in input("Enter multiple value: ").split()]
n=len(x)
y=[]
for i in range(0,n):
    k=True
    c=x[i]
    for j in range(i+1,n):
        if(c<x[j]):
            k=False 
    if(k==True):
        y.append(c)
print(y)