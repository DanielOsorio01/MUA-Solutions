data = input().split()
N, W = int(data[0]), int(data[1])

weights = [0]
values = [0]
table = [[0 for j in range(W+1)] for i in range(N+1)]
for i in range(N):
    item_info = input().split()
    weights.append(int(item_info[0]))
    values.append(int(item_info[1]))

for i in range(1,N+1):
    for j in range(1, W+1):
        if weights[i] <= W: # Checks if the item fits
            if j-weights[i] >= 0 and table[i-1][j] < table[i-1][j-weights[i]] + values[i]:
                table[i][j] = table[i-1][j-weights[i]] + values[i]
            else:
                table[i][j] = table[i-1][j]

print(table[N][W])