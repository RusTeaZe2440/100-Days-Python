from functools import lru_cache  # mainly used for code memoization 
#memoization means once code has been runed cache will store the values to be return it will not wait for time.sleep(5) command
import time

# def count_vowels(sentence):
#     sentence = sentence.casefold()
#     return sum(sentence.count(vowel) for vowel in 'aeiou')
# c = count_vowels("we are valorant")
# # print(c)

@lru_cache(maxsize= None)
def fx(n):
    time.sleep(5)
    return n * 5

print(fx(20))
print("Executed for 20")
print(fx(5))
print("Executed for 5")
print(fx(6))
print("Executed for 6")

print(fx(20))
print("Executed for 20")
print(fx(5))
print("Executed for 5")
