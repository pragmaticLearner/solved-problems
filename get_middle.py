def get_middle(s):
    x = len(s)                  # get the length of the string
    y = x//2                    # divide x by 2 and keep as integer (not float)
    print(x)
    print(y)
    if x % 2 == 0:              # IF x is even
        return s[y - 1:y + 1]       # return middle two characters
    else:                       # IF x is not even
        return s[y:y + 1]           # return middle character only


print(get_middle("hello there"))