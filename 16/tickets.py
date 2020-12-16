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
rulenames = []
myticket = []
validtickets = []
error = 0
nearby = False
with open('input') as f:
    for line in f:
        # If a rule
        if ':' in line and line.strip()[-1] != ':':
            rulename = line.split(':')[0].strip()
            rulenames.append(rulename)

            rawrule = line.split(':')[-1].strip()
            rules.append(createrule(rawrule))
            continue

        if 'your ticket:' in line:
            myticket = [int(x) for x in f.readline().strip().split(',')]

        if 'nearby tickets:' in line:
            nearby = True
            continue

        if nearby:
            valid = True
            for number in line.strip().split(','):
                for rule in rules:
                    if rule(int(number)):
                        break
                if not rule(int(number)):
                    error += int(number)
                    valid = False
            if valid:
                validtickets.append([int(x) for x in line.strip().split(',')])

# Create a possibilities dictionary: possible fields per item in the ticket
possibilities = {i: list(range(len(rules))) for i in range(len(myticket))}
# Remove those fields which are not possible (where at least one is not compliant)
for i in range(len(myticket)):
    for r in range(len(rules)):
        possible = True
        for validticket in validtickets:
            if not rules[r](validticket[i]):
                possible = False
                break
        if not possible:
            possibilities[i].remove(r)

# Find out which field is which
ensured = list(range(len(rules)))
while True:
    # Those items with a single possibility are ensured to be that field.
    for candidates in possibilities.values():
        if len(candidates) == 1:
            candidate = candidates[0]
            if candidate in ensured:
                break

    # Remove that field for all other items
    for candidates in possibilities.values():
        if len(candidates) != 1 and candidate in candidates:
            candidates.remove(candidate)

    # Keep iterating until all items have a single candidate
    ensured.remove(candidate)
    if not len(ensured):
        break

# Multiply the values for the fields the name of which starts with "departure"
departures = 1
for r in range(len(rules)):
    if not rulenames[r].startswith("departure"):
        continue
    for field, order in possibilities.items():
        if order[0] == r:
            departures *= myticket[field]

print(f"The ticket scanning error rate is {error}")
print(f"The departures value is {departures}")
