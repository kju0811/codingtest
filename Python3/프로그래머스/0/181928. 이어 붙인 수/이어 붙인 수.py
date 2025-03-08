def solution(num_list):
    answer = 0
    odd = [i for i in num_list if i%2 != 0]
    even = [j for j in num_list if j%2 == 0]
    
    a = ''.join(map(str,odd))
    b = ''.join(map(str,even))
    
    if 2<= len(num_list) <=10 and all(1<= i <= 9 for i in num_list) and 1<= len(odd) and 1<= len(even):
        return int(a)+int(b)
    