import math
def is_palindrome(x):
    while x !=0:
        if x % 10 == int(x / math.pow(10,int(math.log10(x)))):
            x %= math.pow(10,int(math.log10(x)))
            x %= 10
        else:
            return False
    return True

print is_palindrome(191)
print is_palindrome(192)
print is_palindrome(1192911)
print is_palindrome(1000021)
