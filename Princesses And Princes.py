t = int(input())

for _ in range(t):
    n = int(input())
    princesses = [True]+[False for i in range(n)]
    princes = [True]+[False for i in range(n)]
    flag = False

    for i in range(1, n + 1):
        lst = list(map(int, input().split(" ")))
        for j in range(1, lst[0] + 1):
            if not princesses[i] and not princes[lst[j]]:
                princesses[i] = True
                princes[lst[j]] = True
                break

    for k in range(1, n+1):
        if not princesses[k]:
            flag = True
            print("IMPROVE")
            for l in range(1, n+1):
                if not princes[l]:
                    print(k, l)
                    break
            break

    if not flag:
        print("OPTIMAL")

            

