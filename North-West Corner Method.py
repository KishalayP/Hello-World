import numpy as np
class NWCM:
    def __init__(self):
        #lol
        pass
    def right(s,d,j):
    
            s=int(s)
            d=int(d)
            factor=d
            suu=s-d
            j+=1
            return j,suu,factor

    def down(s,d,i):  

            s=int(s)
            d=int(d)   
            factor=s  
            d=d-s
            i+=1
            return i,d,factor

    def main():

   
        tm1=[]
        row=int(input("Enter the Number of Sources: "))
        column=int(input("Enter the Number of Destinations: "))
        
        for i in range(row):          
            a =[]       
            a=[int(x) for x in input("Enter Cost Matrix Row-Wise: ").split(maxsplit=column)]
            tm1.append(a)

        tm=np.array([tm1])
        tm=tm.reshape(row,column)
        su=[int(x) for x in input("Enter Supplies Data: ").split(maxsplit=row)]
        d=[int(x) for x in input("Enter Demand Data: ").split(maxsplit=column)]
        i,j=0,0
        total_cost=float(0)

        while (i<row and j<column):

            supply=su[i]
            demand=d[j]
            ele=tm[i,j]
            

            if(supply>=demand): 
                
                j_in,s,fact=NWCM.right(supply,demand,j)
                j=j_in
                su[i]=s
                cost=fact*ele
                
                
            elif(supply<demand): 
                
                i_in,s,fact=NWCM.down(supply,demand,i)
                i=i_in
                d[j]=s
                cost=fact*ele
            
            total_cost= cost + total_cost
            print("({}x{})".format(ele,fact)," ",sep='+')
        print(end='=')
        print(total_cost)
        
        print("\n The total cost of Transportation comes to {}".format(total_cost))


if __name__=="__main__":
     NWCM.main()       