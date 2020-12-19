from typing import Dict, List, Union
from re import compile

RULE = 0

with open('input') as f:
    inpt = f.read().strip()

messages: List[str] = [msg for msg in inpt.split(2 * '\n')[1].split()]
rules: Dict[int, Union[str, List[List[int]]]] = {}
for rule in inpt.split(2 * '\n')[0].split('\n'):
    index = int(rule.split(':')[0].strip())
    arg = rule.split(':')[1].strip()
    if '"' in arg:
        rules[index] = arg[1:-1]
    else:
        subrules: List[List[int]] = []
        for order in arg.split('|'):
            subrule = []
            for number in order.split():
                subrule.append(int(number))
            subrules.append(subrule)
        rules[index] = subrules


def getregex(rule: int) -> str:
    desc = rules[rule]
    if isinstance(desc, str):
        return desc
    conditionals = []
    for sub in desc:
        tojoin = []
        for number in sub:
            if number == rule:
                continue
            else:
                tojoin.append(getregex(number))
        if rule in sub:
            rgx = []
            for i in range(1,8):
                joiner = "{" + str(i) + "}"
                rgx.append(f"({joiner.join(tojoin)}{joiner})")
            return f"({'|'.join(rgx)})"
        conditionals.append(''.join(tojoin))
    return f"({'|'.join(conditionals)})"


pattern = compile(f"^{getregex(RULE)}$")
matches = 0
for message in messages:
    matches += 1 if pattern.match(message) else 0
print(f"There are initially {matches} messages matching rule {RULE}")

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

pattern = compile(f"^{getregex(RULE)}$")
matches = 0
for message in messages:
    matches += 1 if pattern.match(message) else 0
print(f"{matches} messages match rule {RULE} after changing rules 8 and 11")
