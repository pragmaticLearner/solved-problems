### A script to test if a string is a palindrome
### from https://www.youtube.com/watch?v=qjuXUWzVO_Q
### 18/05/2020

#def simple_func(a):
 #   a = ''.join([i for i in a if i.isalpha()]).replace(" ", "").lower()
  #  print(a == a[::-1])
#simple_func(["What it a cat I saw?"])

s = "Was it A CaT I saw"

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True
print(is_palindrome('lol'))


def num_palindrome(n):
    a = []
    if len(str(n)) == 1:
        return False
    else:
        for i in str(n):
            a.append(i)
    return a[::] == a[::-1]


print(num_palindrome(244))

