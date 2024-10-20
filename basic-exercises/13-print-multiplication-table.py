def multiplication_table(num):
    for i in range(1, num + 1):
        for j in range(1, 11):
            print(i * j, end=' ')
        print()

multiplication_table(10)
