import random

def pick_random(source, n=1):
    if isinstance(source, int):
        return random.randint(1, source)
    return random.choice(source)

def roll_d6():
    return random.randint(1, 6)