def solution(num_list):
    
    for hap in num_list:
        if num_list[-1] > num_list[-2]:
            hap = num_list[-1] - num_list[-2]
        elif num_list[-1] <= num_list[-2]:
            hap = num_list[-1] * 2
            
        num_list.append(hap)
        return num_list