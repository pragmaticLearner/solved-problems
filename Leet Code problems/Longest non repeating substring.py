def longest_substring(string: str) -> int:
    new_str = ""

    count = 0
    for i, j in enumerate(string):
        if i != j:
            new_str += i

    return new_str


print(longest_substring("asd"))
