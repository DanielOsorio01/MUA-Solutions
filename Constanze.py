def constanzeMachine(s):
    for i, l in enumerate(s):
        if l == 'm' or l == 'w':
            return 0
    ways = [0 for i in range(len(s)+1)]
    ways[0] = 1
    ways[1] = 1
    for i in range(2, len(s)+1):
        if s[i-2:i] == 'uu' or s[i-2:i] == 'nn':
            ways[i] = (ways[i-1] + ways[i-2])%(10**9+7)
        else:
            ways[i] = ways[i-1]
    return ways[-1]%(10**9+7)

s=input()
print(constanzeMachine(s))