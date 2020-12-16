
def createrule(rawrule):
    # Returns two ranges in strings (e.g. 3-1)
    range1, range2 = rawrule.split('or')[0], rawrule.split('or')[1]

    # From a range in a string, returns a list of int (e.g. [3, 1])
    unpack = lambda x: [int(y) for y in x.split('-')]

    # From a list of int, returns a function which returns whether a number is valid
    inrange = lambda x: lambda y: unpack(x)[0] <= y <= unpack(x)[1]

    # From a number, returns whether it is valid in any of the ranges
    return lambda x: inrange(range1)(x) or inrange(range2)(x)

rules = []
error = 0
nearby = False
with open('input') as f:
    for line in f:
        # If a rule
        if ':' in line and line.strip()[-1] != ':':
            rawrule = line.split(':')[-1].strip()
            rules.append(createrule(rawrule))
            continue
        
        if 'nearby tickets:' in line:
            nearby = True
            continue

        if nearby:
            for number in line.strip().split(','):
                for rule in rules:
                    if rule(int(number)):
                        break
                if not rule(int(number)):
                    error += int(number)

print(f"The ticket scanning error rate is {error}")
