# Challenges

""""
THE FAMOUS "FIZZ BUZZ":
Write a program that displays on the console (using a print statement) 
the numbers from 1 to 100 (inclusive, with a line break between each output), 
replacing the following:
- Multiples of 3 with the word "fizz".
- Multiples of 5 with the word "buzz".
- Multiples of both 3 and 5 with the word "fizzbuzz".
"""

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz()

"""
IS IT AN ANAGRAM?
Write a function that takes two words (Strings) and returns true or false (Bool) 
depending on whether they are anagrams or not.
- An Anagram consists of forming a word by rearranging ALL the letters of another initial word.
- It is NOT necessary to check whether both words exist.
- Two identical words are not anagrams.
"""

def anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(anagram("silent", "listen")) # True
print(anagram("Silent", "LISTEN")) # True
print(anagram("Rabbit", "Radios")) # False

"""
THE FIBONACCI SEQUENCE
Write a program that prints the first 50 numbers of the Fibonacci sequence starting at 0.
- The Fibonacci sequence is composed of a series of numbers where the next number is always
the sum of the previous two.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonnacci():
    prev = 0
    next = 1
    for i in range(0, 50):
        print(prev)
        current = prev + next
        prev = next
        next = current

fibonnacci()
        
"""
IS IT A PRIME NUMBER?
Write a program that checks whether a number is prime or not.
Once done, print the prime numbers between 1 and 100.
"""
def prime():
    for i in range(1, 101):
        if i >= 2:
            divisiable = False
            for number in range(2, i):
                if i % number == 0:
                    divisiable = True
                    break
            if not divisiable:
                print(i)

prime()

"""
REVERSE STRINGS
Create a program that reverses the order of a string without using built-in 
functions that do it automatically.
- If we pass "Hello world", it should return "dlrow olleH".
"""

def reverse(sentence):
    length = len(sentence)
    reverse_sentence = ""
    for letter in range(0, length):
        reverse_sentence += sentence[length - letter - 1]
    print(reverse_sentence)
    
reverse("Hello world")