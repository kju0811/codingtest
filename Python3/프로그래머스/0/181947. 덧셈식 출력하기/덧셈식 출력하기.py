a, b = map(int, input().strip().split(' '))

if 1>a or b>100:
    print('a,b의 범위 오류')

print(f'{a} + {b} = {a+b}')