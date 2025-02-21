str = input()

if not (1 <= len(str) <= 20):
    print("str의 길이 오류")
else:
    print(str.swapcase())