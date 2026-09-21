class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            sum=0
            while n!=0:
                dig=n%10
                sum=sum+dig**2
                n=n//10
            n=sum
        return n==1
        
