from typing import Literal

from pyperclip import copy
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

from gen_experimental import experimental
from gen_theoretical import theoretical

def plot_distribution(distribution: dict[int, float], hand_size: int, *, experimental: bool) -> None:
    plt.figure(figsize=(20, 15))
    plt.ylim(top=0.35)
    plt.bar(distribution.keys(), distribution.values(), tick_label=distribution.keys())
    plt.xlabel('\nNumber of cards drawn until a match (x)')
    plt.ylabel('Probability of success on the x-th draw [P(X = x)]\n')
    plt.savefig(f'./out/{'experimental' if experimental else 'theoretical'}_{hand_size}.png')
    plt.close()

def simulate(hand_size: Literal[4, 6], *, iterations: int) -> None:
    exp = experimental(iterations, hand_size=hand_size)
    theo = theoretical(hand_size)

    table = (
        f'| {'x':<2} | Experimental | Theoretical | Difference |\n'
        f'|{'-' * 4}|{'-' * 14}|{'-' * 13}|{'-' * 12}|\n'
    ) + '\n'.join(
        f'| {x:>2} | {p_e:<12.8f} | {p_t:<11.8f} | {abs(p_e - p_t):>10.8f} |'
        for (x, p_e), p_t in zip(exp.items(), theo.values())
    )

    copy(table)
    print(table)

    plot_distribution(exp, hand_size, experimental=True)
    plot_distribution(theo, hand_size, experimental=False)

if __name__ == '__main__':
    ITERATIONS = 10_000_000

    #simulate(4, iterations=ITERATIONS)
    simulate(6, iterations=ITERATIONS)