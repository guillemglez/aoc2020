count = 0
with open("input") as f:
    for line in f:
        # 1-3 a: abcde
        # 1-3 b: cdefg
        # 2-9 c: ccccccccc
        nums = line.split()[0]
        minnum = int(nums.split("-")[0])
        maxnum = int(nums.split("-")[1])
        letter = nums = line.split()[1][0]
        password = line.split()[2]

        occurrences = password.count(letter)
        if minnum <= occurrences <= maxnum:
            count += 1

print(f"There are {count} correct passwords.")
