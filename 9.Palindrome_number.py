def isPalindrome(x: int) -> bool:
        x=str(x)
        return x[::-1]==x
    
x = 121
print(isPalindrome(x))