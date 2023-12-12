import random


def get_random_winners(quantity, participants: dict):
    if quantity > len(participants):
        return []

    keys_list = list(participants.keys())
    print(keys_list)
    random.shuffle(keys_list)
    return random.sample(keys_list, k=quantity)