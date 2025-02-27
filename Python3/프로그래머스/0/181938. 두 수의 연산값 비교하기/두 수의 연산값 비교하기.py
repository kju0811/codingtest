def solution(a, b):
    sum = str(a) + str(b)
    mul = 2*a*b
    if 1<= a and b<10000:
        if int(sum) >= mul:
            return int(sum)
        else:
            return mul
        
        