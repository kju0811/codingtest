def solution(num_list):
    answer = 1
    sum = 0
    mul = 1
    
    if not(2<= len(num_list) <= 10 and all(1<= i <=9 for i in num_list)):
        return 3

    for i in num_list:
            answer *= i 
            sum += i
            mul = sum**2

    if answer < mul:
        return 1
    elif answer > mul:
        return 0
        
 