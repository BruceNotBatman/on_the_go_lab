def reverse(s):
    new_str = "" 

    for i in range (len(s)):
        new_str += s[len(s)- i - 1]
    return new_str

trial =input("Give me a word: ")

print(reverse(trial))

def palindrome(p):
    new_str = reverse(p) 
    if p == new_str:
        return True 
    else:
        return False  

print(palindrome("boob"))