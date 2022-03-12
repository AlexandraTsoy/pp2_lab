n = int(input())
demon = {}
hunter = {}
cnt = 0

for i in range(n):
    demon_name, weakness = input().split()
    if demon.get(weakness) == None:
        demon[weakness] = 1
    else:
        demon[weakness] += 1

m = int(input())

for j in range(m):
    hunter_name, ability, kill = input().split()
    z = int(kill)
    if demon.get(ability) == None:
        hunter[ability] = z
    else:
        demon[ability] -= z

for i in demon.values():
    if i > 0:
        cnt += i
print("Demons left:", cnt)