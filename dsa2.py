class solution:
    def evenly_divides(self, N):
        count=0
        A=N
        while N>0:
            digit=N%10
            if digit!=0:
                if A%digit==0:
                    count+=1
            N=N//10
        return count
        
        
        pass
