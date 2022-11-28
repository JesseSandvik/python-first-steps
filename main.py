def fibonacci():
    a = 0
    b = 1
    while a < 50:
        print(a)
        temp = b
        b = a + b
        a = temp

fibonacci()