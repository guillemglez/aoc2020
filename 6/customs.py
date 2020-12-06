from typing import Dict

ABC: str = 'abcdefghijklmnopqrstuvwxyz'

with open('input') as f:
    inpt: str = f.read()

counts = 0
for group in inpt.split('\n\n'):
    questions: Dict[str, bool] = {k: False for k in ABC}
    for question in group:
        if question in questions.keys():
            questions[question] = True
    count = list(questions.values()).count(True)
    counts += count

print(f'The sum of counts is {counts}')
