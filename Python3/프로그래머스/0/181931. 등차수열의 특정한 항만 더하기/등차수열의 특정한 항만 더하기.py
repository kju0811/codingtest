def solution(a, d, included):
    result = 0
    
    if 1<= a <= 100 and 1<= d <= 100 and 1<= len(included) <= 100 and any(included):
        for i in range(len(included)):
            if included[i] == True:
                result += a + d * i
        return result