with open('input') as f:
    arrival = int(f.readline().strip())
    ids = f.readline().strip().split(',')

buses = [int(x) for x in ids if x != 'x']
offsets = [i for i, x in enumerate(ids) if x != 'x']

waiting = {'id': 0, 'time': float('inf')}
for bus in buses:
    t = 0
    while t < arrival:
        t += bus
    if t - arrival < waiting['time']:
        waiting = {'id': bus, 'time': t - arrival}

span, time, lastbus = 1, 0, 1
for bus, offset in zip(buses, offsets):
    span *= lastbus
    while (time + offset) % bus != 0:
        time += span
    lastbus = bus

print(
    f"The result for the shortest waiting time is {waiting['id'] * waiting['time']}"
)
print(f"The gold coin contest answer is {time}")
