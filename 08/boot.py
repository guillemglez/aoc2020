from typing import List, Tuple, Dict

with open('input') as f:
    inpt = f.read()

code: List[Tuple[str, int]] = []
for rawinstruction in inpt.split('\n'):
    operation = rawinstruction.split()[0]
    argument = int(rawinstruction.split()[1])
    code.append((operation, argument))

def run(code: List[Tuple[str, int]]) -> int:
    ran: Dict[int, bool] = {i: False for i in range(len(code))}
    accumulator: int = 0
    line: int = 0
    while line < len(code) and not ran[line]:
        ran[line] = True
        op, arg = code[line]
        if op == 'acc':
            accumulator += arg
        if op == 'jmp':
            line += arg - 1
        line += 1
    return accumulator

def ishealthy(code: List[Tuple[str, int]]) -> bool:
    ran: Dict[int, bool] = {i: False for i in range(len(code))}
    line: int = 0
    while line < len(code):
        if ran[line]:
            return False
        else:
            ran[line] = True
        op, arg = code[line]
        if op == 'jmp':
            line += arg - 1
        line += 1
    return line == len(code)

for line, instruction in enumerate(code):
    op, arg = instruction
    if op == 'acc':
        continue
    fixed = code.copy()
    fixed[line] = ('jmp' if op == 'nop' else 'nop', arg)
    if ishealthy(fixed):
        break
    
print(f"When broken, it crashes with the accumulator value being {run(code)}.")
print(f"Once fixed, it exits with the accumulator value being {run(fixed)}.")
