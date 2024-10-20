def digits_in_reverse_order(num):
    num_s = str(num)
    num_s_rv = num_s[::-1]
    
    return " ".join(list(num_s_rv))

print(digits_in_reverse_order(7536))
