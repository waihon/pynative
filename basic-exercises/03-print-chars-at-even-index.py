str = input("Enter a string: ")

print("Original String is ", str)
print("Printing only even index chars")

for i, char in enumerate(str):
    if i % 2 == 0:
        print(char)
