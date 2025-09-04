# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', 
# and they can appear in both lower and upper cases, 
# more than once.


def reverseVowels(s: str) -> str:
    word = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', I]
    vowels_word = []
    result = ''

    for i in range(len(word)): 
        if word[i] in vowels: 
            vowels_word.append(word[i]) 
    
    vowels_word.reverse() 

    count = 0
    for i in range(len(word)): 
        if word[i] in vowels: 
            word[i] = vowels_word[count]
            count += 1

    for i in range(len(word)): 
        result += word[i]

    return result
print(reverseVowels('abe'))