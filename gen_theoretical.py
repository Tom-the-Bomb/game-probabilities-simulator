from typing import Callable, Literal
from math import prod

def prod_f(x: int, f: Callable[[int], int]) -> float:
    return prod(f(k) for k in range(1, x))

def P_4(x: int) -> float:
    """Probability function for drawing 4 cards"""
    return (96 * (
        8 * prod_f(x, lambda k: 45 - k)
        + 528 * prod_f(x, lambda k: 41 - k)
        + 9 * prod_f(x, lambda k: 45 - k)
        + 1_760 * prod_f(x, lambda k: 37 - k)
    )) / (20_825 * prod_f(x + 1, lambda k: 49 - k))

def P_6(x: int) -> float:
    """Probability function for drawing 6 cards"""
    return (2 * (
        9 * prod_f(x, lambda k: 45 - k)
        + 396 * prod_f(x, lambda k: 41 - k)
        + 12 * prod_f(x, lambda k: 45 - k)
        + 4_752 * prod_f(x, lambda k: 41 - k)
        + 35_200 * prod_f(x, lambda k: 37 - k)
        + 1_782 * prod_f(x, lambda k: 41 - k)
        + 118_800 * prod_f(x, lambda k: 37 - k)
        + 665_280 * prod_f(x, lambda k: 33 - k)
        + 608_256 * prod_f(x, lambda k: 29 - k)
    )) / (195_755 * prod_f(x + 1, lambda k: 47 - k))

def E(hand_size: Literal[4, 6]) -> float:
    """Expected value function"""
    return sum(
        x * (P_4(x) if hand_size == 4 else P_6(x))
        for x in range(1, 52 - hand_size + 1)
    )

def theoretical(*, hand_size: Literal[4, 6]) -> dict[int, float]:
    """Generates the theoretical distribution"""
    return {
        x: P_4(x) if hand_size == 4 else P_6(x)
        for x in range(1, 52 - hand_size + 1)
    }