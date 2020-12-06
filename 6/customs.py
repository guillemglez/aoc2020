from typing import Dict, List

ABC: str = 'abcdefghijklmnopqrstuvwxyz'

with open('input') as f:
    inpt: str = f.read()

count = 0
for group in inpt.split('\n\n'):
    people: List[str] = group.split()
    questions: List[str] = [q for q in people.pop()]

    for person in people:
        for question in questions.copy():
            if question not in person:
                questions.remove(question)

    count += len(questions)

print(f'The sum of counts is {count}')
