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


def evaluate2(expression: str) -> int:
    while SUM in expression:
        left = None
        right = None
        for i, piece in enumerate(expression.split()):
            if piece == SUM:
                li = 1
                lparentheses, rparentheses = 0, 0
                left = expression.split()[i - li]
                while left.count(')') != left.count('('):
                    if left.count('(') > left.count(')'):
                        left = left[1:]
                        lparentheses += 1
                        continue
                    li += 1
                    left = ' '.join((expression.split()[i - li], left))

                ri = 1
                right = expression.split()[i + ri]
                while right.count(')') != right.count('('):
                    if right.count('(') < right.count(')'):
                        right = right[:-1]
                        rparentheses += 1
                        continue
                    ri += 1
                    right = ' '.join((right, expression.split()[i + ri]))

                sumresult = str(evaluate2(left) + evaluate2(right))
                if lparentheses != rparentheses:
                    if lparentheses > rparentheses:
                        lparentheses -= rparentheses
                        rparentheses = 0
                    else:
                        rparentheses -= lparentheses
                        lparentheses = 0
                    sumresult = lparentheses * '(' + sumresult + ')' * rparentheses

                expression = ' '.join((*expression.split()[:i - li], sumresult,
                                       *expression.split()[i + ri + 1:]))
                break
    return evaluate(expression)


result = 0
result2 = 0
with open('input') as f:
    for line in f:
        result += evaluate(line.strip())
        result2 += evaluate2(line.strip())

print(f"The sum of the resulting values is {result}")
print(
    f"The sum of the resulting values is {result2} once the new rules are applied"
)
