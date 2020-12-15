from typing import Dict, List, Tuple

INPUT: List[int] = [0, 12, 6, 13, 20, 1, 17]

game: Dict[int, Tuple[int, int]] = {}
lastnumber: int = -1
for play in range(2020):
    if play < len(INPUT):
        number = INPUT[play]
    else:
        number = game[lastnumber][1] - game[lastnumber][0]

    if number not in game.keys():
        game[number] = play, play
    else:
        game[number] = game[number][1], play
    lastnumber = number

print(f"The 2020th number will be {lastnumber}")
