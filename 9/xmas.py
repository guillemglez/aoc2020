from typing import List

header: List[int] = []
with open('input') as f:
    for line in f:
        if len(header) <= 25:
            header.append(int(line))
            continue

        valid: List[int] = []
        for one in header:
            for another in header:
                if not one == another:
                    valid.append(one + another)

        if int(line) not in valid:
            print(
                f"The fist number not sticking to the rule is {line.strip()}")
            break

        header.pop(0)
        header.append(int(line))
