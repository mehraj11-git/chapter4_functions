def is_palindrom(word):
    reverse_word=word[::-1]
    if word==reverse_word:
        return True
    return False
print(is_palindrom("madam"))
print(is_palindrom("mehraj"))
# short from
def is_palindrom(word):
    if word==word[::-1]:
     return True
    return False
print(is_palindrom("sharat"))
print(is_palindrom("kahn"))
# very short form
def is_palindroms(word):
   return word==word[::-1]
print(is_palindrom("yooy"))
print(is_palindrom("amuma")) 


# define is_palindrome func that take one word in string as input
# and return True if it is palindrome else return False

# palindrome --> word that reads same backwards as forwards    ---> madam
