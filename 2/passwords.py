count1 = 0
count2 = 0
with open("input") as f:
    for line in f:
        # 1-3 a: abcde
        # 1-3 b: cdefg
        # 2-9 c: ccccccccc
        nums = line.split()[0]
        firstnum = int(nums.split("-")[0])
        secondnum = int(nums.split("-")[1])

        letter = line.split()[1][0]
        password = line.split()[2]

        occurrences = password.count(letter)
        if firstnum <= occurrences <= secondnum:
            count1 += 1

        firstpos = password[firstnum - 1]
        secondpos = password[secondnum - 1]

        if (firstpos is letter or secondpos is letter
            ) and not (firstpos is letter and secondpos is letter):
            count2 += 1

print(f"There are {count1} correct passwords following the first policy.")
print(f"There are {count2} correct passwords following the second policy.")
