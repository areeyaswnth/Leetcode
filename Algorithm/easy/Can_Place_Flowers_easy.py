# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if(i==0 and flowerbed[0]==0 ):
                    if((len(flowerbed)>1 and flowerbed[1]==0)or (len(flowerbed)<=1 )):
                        flowerbed[0]=1
                        n-=1
            elif(i==len(flowerbed)-1 and flowerbed[-1]==0 and flowerbed[-2]==0):
                    flowerbed[-1]=1
                    n-=1            
            elif(i-1>0 and i+1<len(flowerbed)):
                if(flowerbed[i+1]==0 and flowerbed[i]==0 and flowerbed[i-1]==0):
                    flowerbed[i]=1
                    n-=1
            if(n<=0):
                return True
        if(n<=0):
                return True
        else:
                return False   
   