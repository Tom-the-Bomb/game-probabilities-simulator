from typing import Literal

from pyperclip import copy
from matplotlib import pyplot as plt

from gen_experimental import experimental
from gen_theoretical import theoretical, E

def plot_distribution(distribution: dict[int, float], hand_size: int, *, experimental: bool) -> None:
    plt.style.use('fivethirtyeight')
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['figure.facecolor'] = 'white'

    plt.figure(figsize=(20, 15))
    plt.ylim(top=0.35)
    plt.bar(distribution.keys(), distribution.values(), tick_label=distribution.keys())
    plt.xlabel('\nNumber of cards drawn until a match (x)')
    plt.ylabel('Probability of success on the x-th draw [P(X = x)]\n')
    plt.box(False)
    plt.savefig(f'./out/{'experimental' if experimental else 'theoretical'}_{hand_size}.png')
    plt.close()

def simulate(hand_size: Literal[4, 6], *, iterations: int | None = None) -> None:
    theo = theoretical(hand_size=hand_size)

    if iterations is not None:
        exp = experimental(iterations, hand_size=hand_size)

        table = (
            f'| {'x':<2} | Experimental | Theoretical | {'Error':<10} |\n'
            f'|{'-' * 4}|{'-' * 14}|{'-' * 13}|{'-' * 12}|\n'
        ) + '\n'.join(
            f'| {x:<2} | {p_e:<12.8f} | {p_t:<11.8f} | {abs(p_e - p_t):<10.8f} |'
            for (x, p_e), p_t in zip(exp.items(), theo.values())
        )

        plot_distribution(exp, hand_size, experimental=True)
    else:
        table = (
            f'| {'x':<2} | Theoretical |\n'
            f'|{'-' * 4}|{'-' * 13}|\n'
        ) + '\n'.join(
            f'| {x:<2} | {p_t:<11.8f} |'
            for x, p_t in theo.items()
        )

    copy(table)

    print(f'\nTable of probability values for [{hand_size = }]')
    print(table)
    print(f'\nExpected Value: E_{hand_size}(X) = {E(hand_size):.8f}')

    plot_distribution(theo, hand_size, experimental=False)

if __name__ == '__main__':
    ITERATIONS = 20_000_000

    simulate(4, iterations=ITERATIONS)
    #simulate(6, iterations=ITERATIONS)