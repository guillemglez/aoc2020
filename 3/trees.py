with open("input") as f:
    x = 0
    trees = 0
    for line in f:
        char = x % (len(line) - 1)  # ignore \n

        if line[char] == "#":
            trees += 1

        x += 3

print(f"You have encountered {trees} trees")
