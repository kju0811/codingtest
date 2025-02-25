str1, str2 = input().strip().split(' ')
if not(1<=len(str1) or len(str2)<=10):
    print("str 길이 오류")
print(str1+str2)