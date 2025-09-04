from typing import List

# You have a long flowerbed in which some of the plots are planted, 
# and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, 
# where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    for i in range(len(flowerbed)):
        item = flowerbed[i]
        if(item == 1 and i < len(flowerbed) - 1): 
            flowerbed[i+1] = 'X'
            flowerbed[i-2] = 'X'
    

    count = 0 
    for i in range(len(flowerbed)):
        item = flowerbed[i]
        if(item == 0 and i < len(flowerbed) - 1): 
            if(flowerbed[i+1] != 1 and flowerbed[i-2] != 1):
                flowerbed[i+1] = 'X'
                flowerbed[i-2] = 'X'
                flowerbed[i] = 1
                count += 1
            if(flowerbed[i+1] == 'X' and flowerbed[i-2] == 'X'):
                flowerbed[i] = 1
                count += 1
    
    print(flowerbed)
    return count == n


print(canPlaceFlowers([1,0,0,0,1], 1))
