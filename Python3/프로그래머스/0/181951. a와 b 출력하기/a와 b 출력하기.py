a, b = map(int, input().strip().split(' '))

while True:
    if -1000000 <= a and b <= 1000000:
        print(f'a = {a} \nb = {b}')
        break
    else:
        continue
    