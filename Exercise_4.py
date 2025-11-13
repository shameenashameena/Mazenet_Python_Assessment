# Exercise 4: Dictionary Comprehension
words = ["apple", "banana", "cherry", "date"]

vowels = "aeiouAEIOU"
vowel_count = {word: sum(1 for char in word if char in vowels) 
               for word in words}

print(vowel_count)
