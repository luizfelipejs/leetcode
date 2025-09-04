
# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, 
# append the additional letters onto the end of the merged string.
# Return the merged string.

def mergeAlternately(word1: str, word2: str) -> str:
    total_size = len(word1 + word2) 
    final_word = "" 
    for i in range(0, total_size): 
        if(len(word1) > i): 
            final_word += word1[i]
        if(len(word2) > i): 
            final_word += word2[i]
        
    return final_word  

print(mergeAlternately("abc", "pqr")) 

print(mergeAlternately("ab", "pqrs")) 

print(mergeAlternately("abcd", "pq")) 