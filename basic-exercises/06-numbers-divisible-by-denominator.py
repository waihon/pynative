def numbers_divisible_by(denominator, lst):
    print("Given list is", lst)
    print("Divisible by", denominator)
    
    for num in lst:
        if num % denominator == 0:
            print(num)

numbers = [10, 20, 33, 46, 55]
numbers_divisible_by(5, numbers)
