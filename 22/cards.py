from typing import List, Dict
import numpy as np

with open('input') as f:
    inpt = f.read().strip()


def parseInput() -> Dict[int, List[int]]:
    decks: Dict[int, List[int]] = {}
    # Parse input
    for rawplayer in inpt.split('\n\n'):
        deck: List[int] = []
        for line in rawplayer.split('\n'):
            if "Player" in line:
                continue
            deck.append(int(line))
        if "Player 1" in rawplayer:
            decks[1] = deck
        if "Player 2" in rawplayer:
            decks[2] = deck
    return decks


def game(decks: Dict[int, List[int]], recursive=False) -> int:
    hands = {k: [v.copy()] for k, v in decks.items()}
    while len(decks[1]) and len(decks[2]):
        play: Dict[int, int] = {}
        for player in decks.keys():
            play[player] = decks[player].pop(0)

        winner = 1 if play[1] > play[2] else 2
        if recursive:
            if all(play[player] <= len(decks[player]) for player in play.keys()):
                winner = game({k: v.copy()[:play[k]]
                                for k, v in decks.items()}, recursive)

        if winner == 1:
            decks[1] += [card for card in play.values()]
        else:
            decks[2] += [card for card in reversed(play.values())]

        if recursive:
            for player in hands.keys():
                if any(decks[player] == hand for hand in hands[player]):
                    return 1
                else:
                    hands[player].append(decks[player].copy())
        

    return 1 if len(decks[1]) else 2


def score(decks: Dict[int, List[int]], winner: int) -> int:
    score = 0
    for points, card in enumerate(reversed(decks[winner])):
        score += (points + 1) * card
    return score


decks = parseInput()
print(
    f"The winning player's score is {score(decks, game(decks, recursive=False))}"
)
decks = parseInput()
print(
    f"The Recursive Combat champion's score is {score(decks, game(decks, recursive=True))}"
)
