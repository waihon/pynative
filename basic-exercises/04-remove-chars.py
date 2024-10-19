def remove_chars(str, first_n):
    size = len(str)
    if first_n < size:
        return str[first_n::]
    else:
        return str

print(remove_chars("PYnative", 2)) # native
print(remove_chars("PYnative", 4)) # tive
print(remove_chars("PYnative", 7)) # e
print(remove_chars("PYnative", 8)) # PYnative
