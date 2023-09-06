new_ways_1, new_ways_2 = 1, 1
temp = -1
temp = new_ways_2
new_ways_2 = temp + new_ways_1
new_ways_1 = temp

for i in range(10):
    print(new_ways_2)
    temp = new_ways_2
    new_ways_2 = temp + new_ways_1
    new_ways_1 = temp