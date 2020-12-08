from typing import List, Tuple, Dict

with open('input') as f:
    inpt = f.read()

code: List[Tuple[str, int]] = []
for instruction in inpt.split('\n'):
    operation = instruction.split()[0]
    argument = int(instruction.split()[1])
    code.append((operation, argument))

ran: Dict[int, bool] = {i: False for i in range(len(code))}
accumulator: int = 0
line: int = 0
while not ran[line]:
    ran[line] = True
    op, arg = code[line]
    if op == 'acc':
        accumulator += arg
    if op == 'jmp':
        line += arg
        continue
    line += 1
    
print(f"The accumulator value is {accumulator}")
