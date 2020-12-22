from typing import List, Dict

with open('input') as f:
    inpt = f.read().strip()

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

while len(decks[1]) and len(decks[2]):
    play: Dict[int, int] = {}
    for player in decks.keys():
        play[player] = decks[player].pop(0)
    if play[1] > play[2]:
        decks[1] += [card for card in play.values()]
    else:
        decks[2] += [card for card in reversed(play.values())]

winner = decks[1] if len(decks[1]) else decks[2]
score = 0
for points, card in enumerate(reversed(winner)):
    score += (points + 1) * card

print(f"The winning player's score is {score}")
