def merge_two_lists(num_lst1, num_lst2):
    odd_nums = list(filter(lambda x: x % 2 == 1, num_lst1))
    even_nums = list(filter(lambda x: x % 2 == 0, num_lst2))
    
    return odd_nums + even_nums

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("Result list", merge_two_lists(list1, list2))
