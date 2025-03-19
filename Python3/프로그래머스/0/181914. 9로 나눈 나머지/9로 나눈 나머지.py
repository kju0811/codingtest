def solution(number):
    answer = 0
    if not(int(number) <0):
        answer = eval('+'.join(number))
        answer %=9
    return answer