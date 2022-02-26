arr = []
a = int(input())

for i in range(a):
    i = int(input())
    arr.append(i)

for i in range(a):
    if arr[i] <= 10:
        print('Go to work!')
    elif arr[i] <= 25:
        print('You are weak')
    elif arr[i] <= 45:
        print('Okay, fine')
    else:
        print('Burn! Burn! Burn Young!')