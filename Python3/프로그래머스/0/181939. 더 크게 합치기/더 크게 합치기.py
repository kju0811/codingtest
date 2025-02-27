def solution(a, b):
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    if 1<= a and b<10000:
        if str1 >= str2:
            return int(str1)
        else:
            return int(str2)