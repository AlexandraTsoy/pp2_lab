plrs = []

while True:
    n = int(input())
    if n == 0:
        break
    plrs.append(n)

ans = []

while len(plrs) > 0:
    x = plrs[0] + plrs[-1]
    ans.append(x)
    plrs.pop(0)
    plrs.pop(-1)
    if len(plrs) == 1:
        ans.append(plrs[0])
        plrs.pop(0)
        break

for i in ans:
    print(i, end = ' ')