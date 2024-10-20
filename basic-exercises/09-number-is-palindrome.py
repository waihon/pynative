def number_is_palindrome(num):
    print("Original number", num)
    
    num_s = str(num)
    num_s_reversed = num_s[::-1]
    
    if num_s == num_s_reversed:
        yes_no = "Yes"
        is_not = "is"
    else:
        yes_no = "No"
        is_not = "is not"

    print(yes_no, ". The given numebr", is_not, "palindrome number.")

number_is_palindrome(121)   # Yes
number_is_palindrome(12321) # Yes
number_is_palindrome(125)   # No
number_is_palindrome(12345) # No
