import random 

names =["Emmanuel", "Michaiah", "Rukky"]

def randomize_names():
    random.shuffle(names)
    return names


def get_random_number():
    return  random.random(1, 100)