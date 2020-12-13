with open('input') as f:
    arrival = int(f.readline().strip())
    buses = [int(x) for x in f.readline().strip().split(',') if x != 'x']

waiting = {'id': 0, 'time': float('inf')}
for bus in buses:
    t = 0
    while t < arrival:
        t += bus
    if t - arrival < waiting['time']:
        waiting = {'id': bus, 'time': t - arrival}

print(
    f"The result for the shortest waiting time is {waiting['id'] * waiting['time']}"
)
