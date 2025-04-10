import random

from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

from tqdm import tqdm

def draw_card(cards: list[int]) -> int:
    return cards.pop(random.randrange(0, len(cards)))

def draw_hand(cards: list[int], hand_size: int) -> set[int]:
    return {draw_card(cards) for _ in range(hand_size)}

def main(iterations: int, *, hand_size: int) -> None:
    distribution = {i: 0 for i in range(1, 52 - hand_size + 1)}

    for _ in tqdm(range(iterations)):
        cards = list(range(1, 14)) * 4
        hand = draw_hand(cards, hand_size)

        count = 0
        while draw_card(cards) not in hand:
            count += 1

            if not cards:
                break
        else:
            count += 1

        distribution[count] += 1

    for x, p in distribution.items():
        print(f'P({x}) = {p}')

    plt.figure(figsize=(18, 12))
    plt.bar(distribution.keys(), distribution.values(), tick_label=distribution.keys())
    plt.savefig('experimental.png')
    plt.close()

if __name__ == '__main__':
    main(5_000_000, hand_size=4)