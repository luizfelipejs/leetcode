from typing import List

# You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, 
# where 0 means empty and 1 means not empty, and an integer n, 
# return true if n new flowers can be planted in the flowerbed 
# without violating the no-adjacent-flowers rule and false otherwise.

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result = []
    for item in candies: 
        candiemax = item + extraCandies
        if(candiemax >= max(candies)): 
            result.append(True)
        else: 
            result.append(False)
    return result

kidsWithCandies([2,3,5,1,3], 3)