from random import randrange

def gimme_number():
    return randrange(5, 26, 5)
    # would do the same as choice(5, 10, 15, 20, 25)

print(gimme_number())
