str, n = input().strip().split(' ')
n = int(n)

if not (1 <= len(str) <= 10):
    print('str의 길이 오류')
elif not (1 <= n <= 5):
    print('n의 길이 오류')
else:
    print(str * n)