def solution(my_string, is_suffix):
    answer = 0
    l = []
    for i in range(len(my_string)):
        l.append(my_string[-i:])
        
    if is_suffix in l:
        return 1
    else:
        return 0
