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
        conditionals.append(''.join([getregex(x) for x in sub]))
    return f"({'|'.join(conditionals)})"


pattern = compile(f"^{getregex(RULE)}$")
matches = 0
for message in messages:
    matches += 1 if pattern.match(message) else 0

print(f"There are {matches} messages matching rule {RULE}")
