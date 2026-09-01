class solution:
    def calculateDigitSum(self,N1, N2):
        sum1=0
        #sum2=0
        for i in range(N1,N2+1):
           n=i
           while n>0:
               digit=n%10
               sum1+=digit
               n=n//10
        return sum1
        
        
        pass
