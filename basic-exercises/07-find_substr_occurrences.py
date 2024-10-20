def find_substr_occurrences(substr, str):
    n = 0
    
    idx = str.find(substr)
    while idx != -1:
        n += 1
        idx = str.find(substr, idx + 1)
    
    print(substr, "appeared", n, "times")

find_substr_occurrences("Emma", "Emma is good developer. Emma is a writer")
