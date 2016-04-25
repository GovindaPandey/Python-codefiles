#Program to find if the string is palindrome
#Date 25/04/2016 15:57
def isPal(s):
    if(len(s) <= 1):
        return True
    else: return s[0] == s[-1] and isPal(s[1:-1])

    
 


