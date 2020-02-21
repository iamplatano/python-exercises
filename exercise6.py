import math
str = input("Enter a string ")

def isPalindrome(str):
    revstr = str[::-1]
    print(revstr)
    if revstr == str:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")        
print(isPalindrome(str))
