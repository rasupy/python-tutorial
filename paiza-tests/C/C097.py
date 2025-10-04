N, X, Y = map(int, input().split())
for i in range(N):
    i += 1
    if i % X == 0 and i % Y == 0:
        print("AB")
    elif i % X == 0:
        print("A")
    elif i % Y == 0:
        print("B")
    else:
        print("N")
