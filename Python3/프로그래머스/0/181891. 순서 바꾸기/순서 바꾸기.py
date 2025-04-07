def solution(num_list, n):
    answer = []
    for i,j in enumerate(num_list):
        answer = num_list[n:] + num_list[:n]
    return answer