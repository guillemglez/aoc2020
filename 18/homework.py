from typing import Optional

MULTIPLICATION = "*"
SUM = "+"


def operate(first: Optional[int], second: int, operator: str) -> int:
    if first is None:
        return second

    if operator == MULTIPLICATION:
        return first * second
    if operator == SUM:
        return first + second
    else:
        raise Exception(f"Wrong operator {operator}")


def evaluate(expression: str) -> int:
    result = None
    operator = None
    subexpression = None
    for piece in expression.split():
        if subexpression is not None:
            subexpression += ' ' + piece
            if subexpression.count(')') > subexpression.count('('):
                result = operate(result, evaluate(subexpression[:-1]),
                                 operator)
                subexpression = None
            continue

        if piece[0] in "0123456789":
            if result is None:
                result = int(piece)
            else:
                result = operate(result, int(piece), operator)

        if piece in (MULTIPLICATION, SUM):
            operator = piece

        if piece[0] == '(':
            subexpression = piece[1:]

    assert result is not None
    return result


result = 0
with open('input') as f:
    for line in f:
        result += evaluate(line.strip())

print(f"The sum of the resulting values is {result}")
