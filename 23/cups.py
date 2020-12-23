from typing import List

inpt = "614752839"


def cups(labeling: str, moves: int = 100) -> str:
    cups = [int(c) for c in labeling]
    current = 0
    move = 0
    aside = []
    while (move < moves):
        move += 1
        currlabel = cups[current]
        # Take next three
        for _ in range(3):
            if (current + 1) < len(cups):
                aside.append(cups.pop(current + 1))
            else:
                aside.append(cups.pop(0))
                current -= 1
        # Find destination
        destlabel = cups[current] - 1
        while not destlabel in cups:
            destlabel -= 1
            if destlabel < min(cups):
                destlabel = max(cups)
                break
        destination = cups.index(destlabel)
        # Place in destination
        while len(aside):
            cups.insert(destination + 1, aside.pop())
        # Next current
        current = cups.index(currlabel) + 1
        if current == len(cups):
            current = 0

    # Find number one
    one = cups.index(1)
    return ''.join([str(x) for x in (cups[one + 1:] + cups[:one])])


print(f"The labels on the cups are {cups(inpt, 100)}")
