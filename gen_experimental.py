from typing import Literal
import random

from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

from tqdm import tqdm

def draw_card(cards: list[int]) -> int:
    return cards.pop(random.randrange(0, len(cards)))

def draw_hand(cards: list[int], hand_size: int) -> set[int]:
    return {draw_card(cards) for _ in range(hand_size)}

def experimental(iterations: int, *, hand_size: Literal[4, 6]) -> dict[int, float]:
    distribution = {i: 0 for i in range(1, 52 - hand_size + (hand_size == 4) + 1)}

    for _ in tqdm(range(iterations), desc=f'Running experimental simulation [{hand_size = }]'):
        cards = list(range(1, 14)) * 4
        hand = draw_hand(cards, hand_size)

        count = 1
        while draw_card(cards) not in hand:
            count += 1

            if not cards and hand_size == 4:
                count = 49
                break

        distribution[count] += 1 / iterations

    return distribution