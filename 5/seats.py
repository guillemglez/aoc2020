with open('input') as f:
    maxsid = 0
    for line in f:
        line = line.strip()

        step = (1 << 7, 1 << 3)
        row = (0, step[0])
        col = (0, step[1])
        for c in line:
            if c == 'F':
                step = (step[0] / 2, step[1])
                row = (row[0], row[1] - step[0])
            if c == 'B':
                step = (step[0] / 2, step[1])
                row = (row[0] + step[0], row[1])
            if c == 'L':
                step = (step[0], step[1] / 2)
                col = (col[0], col[1] - step[1])
            if c == 'R':
                step = (step[0], step[1] / 2)
                col = (col[0] + step[1], col[1])

        sid = row[0] * 8 + col[0]
        if (sid > maxsid):
            maxsid = sid
    
    print(maxsid)
