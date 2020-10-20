def myround(x, base=250):
    return base * round(x/base)
b=[2500,300,1000,2500,4000,5000,2000,2000,1500]
g=[4000, 400,1200,3000,5000,7000,4000,4000,2000]
p=[3000,400,1200,3000,5000,7000,3000,3000,2000]
yl=[2700, 300,1200,3000,4500,6000,3000,3000,1700]
r=[6500,500,750,3000]
lb=[2500,300,1200,3000,4500,6000,3000,3000,1700]
ly=[5600,2500]
f=['RENT site only: ','RENT with 1 House:','RENT with 2 House:','RENT with 2 House:','RENT with 2 House:','RENT with Hotel:']
jk=True
while jk==True:
    color=input("Enter your card colour: ")
    if color=='b':
        c=int(input("Enter Price of city: "))
        x=lambda x,y:int(x*(y/b[0])) 
        z=[ myround(x(j,c)) for j in b[1:] ]
        print(z)
    elif color.lower()=='g':
        c=int(input("Enter Price of city: "))
        x=lambda x,y:int(x*(y/g[0])) 
        z=[ myround(x(j,c)) for j in g[1:] ]
        print(z)
    elif color.lower()=='p':
        c=int(input("Enter Price of city: "))
        x=lambda x,y:int(x*(y/p[0])) 
        z=[ myround(x(j,c)) for j in p[1:] ]
        print(z)
    elif color.lower()=='yl':
        c=int(input("Enter Price of city: "))
        x=lambda x,y:int(x*(y/yl[0])) 
        z=[ myround(x(j,c)) for j in yl[1:] ]
        print(z)
    elif  color.lower()=='r':
        c=int(input("Enter Price of city: "))
        x=lambda x,y:int(x*(y/r[0])) 
        z=[ myround(x(j,c)) for j in r[1:] ]
        print(z)
    elif color.lower()=='lb':
        c=int(input("Enter Price of city: "))
        x=lambda x,y:int(x*(y/lb[0])) 
        z=[ myround(x(j,c)) for j in lb[1:] ]
        print(z)
    elif color.lower()=='ly':
        c=int(input("Enter Price of city: "))
        x=lambda x,y:int(x*(y/ly[0])) 
        z=[ myround(x(j,c)) for j in ly[1:] ]
        print(z)
    ch=input("Press any key to continue or N to Exit: ")
    if ch.lower()=='n':
        jk=False

