# Array Patterens and Problems
# 1 two Pointer Problems


# Question 1 validate palindrome

# solution 1: two pointer approach

# we will use two pointers, one at the start and one at the end of the string
# we will compare the characters at the two pointers
# if they are not the same, we will return false
# if they are the same, we will move the pointers inward
# if we reach the middle of the string, we will return true

# solution 2: recursion

# we will use a recursive function to check if the string is a palindrome
# if the string is empty or has one character, we will return true

# optimal solution: two pointer approach

# we will use two pointers, one at the start and one at the end of the string
# we will compare the characters at the two pointers
# if they are not the same, we will return false
# if they are the same, we will move the pointers inward
# if we reach the middle of the string, we will return true

# solution 3: iterative approach

# we will use a loop to check if the string is a palindrome
# if the string is empty or has one character, we will return true

def is_palindrome(s:str)->bool:
    print(s)
    ss = "".join(ch.lower() for ch in s if ch.isalpha())
    print(ss)
    start=0
    end=len(ss)-1
    print(start,end,ss)
    while start<end:
        if ss[start] != ss[end]:
            return False
        elif ss[start] == ss[end]:
            start+=1
            end-=1
    
    return True

st= is_palindrome("A man, a plan, a canal: Panama")

print(st)