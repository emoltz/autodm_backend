from enum import Enum, auto
import random
from typing import List


class DiceTypes(Enum):
    D100 = 100
    D20 = 20
    D12 = 12
    D10 = 10
    D8 = 8
    D6 = 6
    D4 = 4


def roll_dice(dice: DiceTypes = DiceTypes.D20, modifier: int = None) -> int:
    if (modifier is not None) and (modifier < 0):
        raise ValueError("Modifier cannot be negative")
    if modifier is not None:
        return random.randint(1, dice.value) + modifier
    else:
        return random.randint(1, dice.value)


def roll_multiple_dice(dice: [DiceTypes], modifiers: [int] = None) -> int:
    if (modifiers is not None) and (len(dice) != len(modifiers)):
        raise ValueError("Number of dice and number of modifiers must match")
    elif modifiers is not None and len(dice) == len(modifiers):
        total = 0
        for i in range(len(dice)):
            total += roll_dice(dice[i], modifiers[i])
        return total
    else:
        total = 0
        for die in dice:
            total += roll_dice(die)
        return total
