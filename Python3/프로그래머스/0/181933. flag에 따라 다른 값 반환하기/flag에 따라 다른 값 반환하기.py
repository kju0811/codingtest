def solution(a, b, flag):
    if -1000<= a and b<= 1000:
        if flag == True:
            return a + b
        else:
            return a-b
