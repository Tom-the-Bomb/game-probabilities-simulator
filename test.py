import random
from collections import Counter

from tqdm import tqdm

x = 0
n = 2_000_000

for _ in tqdm(range(n)):
    cards = list(range(1, 14)) * 4

    hand = [cards.pop(random.randrange(0, len(cards))) for _ in range(6)]

    if set(Counter(hand).values()) == {3, 2, 1}:
        x += 1

print(x / n)