def first_last_same(lst):
    first_num = lst[0]
    last_num = lst[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print("Given list:", numbers_x, first_last_same(numbers_x)) # True
print("Given list:", numbers_y, first_last_same(numbers_y)) # False
