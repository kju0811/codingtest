def solution(start_num, end_num):
    answer = []
    for i in range(start_num,end_num +1):
        if 0<=start_num<=end_num<=50:
            i+=1
            answer.append(i-1)
    return answer