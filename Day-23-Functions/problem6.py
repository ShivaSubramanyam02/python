def is_palindrome(s):
    s = str(s)
    return s == s[::-1]



print(is_palindrome(121))