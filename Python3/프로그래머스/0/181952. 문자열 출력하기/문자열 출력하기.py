str = input()

if len(str) < 1 or len(str) >1000000:
    print('str의 길이 오류')
elif ' ' in str:
    print('str에 공백문자 불가')
else:
    print(str)