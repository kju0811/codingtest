a, b = map(int, input().strip().split(' '))

if -1000000 <= a <= 1000000 and -1000000 <= b <= 1000000:
    print(f'a = {a} \nb = {b}')
else:
    print("오류")
    