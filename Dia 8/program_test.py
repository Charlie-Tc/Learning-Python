def number_impair():
    impairs = []

    for num in range(1,6):
        if num % 2 == 1:
            impairs.append(num)

    print(impairs)

def titles(word):
    print(word.title)
