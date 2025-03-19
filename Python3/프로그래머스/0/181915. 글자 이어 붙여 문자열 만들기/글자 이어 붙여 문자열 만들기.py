def solution(my_string, index_list):
    answer = ''
    if 1<=len(my_string)<=1000 and 1<=len(index_list)<=1000 and all(0<= i <len(my_string) for i in index_list):
        for i in index_list:
            answer += my_string[i]
        return answer