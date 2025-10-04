N, L = map(int, input().split())
for _ in range(N):
    x = int(input())
    if x < L:
        L += x // 2
        L = int(L)
    elif x > L:
        L = L // 2
        L = int(L)
    elif x == L:
        pass
print(L)
