class Trans:
    def min_find(penalty):
        n=len(penalty)
        min=penalty[0]
        for i in range(penalty.index(min),n):
            for j in range(i+1,n):
                if(penalty[i]>penalty[j]):
                    min=penalty[j] 
                    break        
        return min
    def main():
        a=[float(i) for i in input("Enter Array: ").split()]
        py=Trans.min_find(a)
        print(py)
    if __name__=="__main__":
        main()


                
