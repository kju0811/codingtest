def solution(arr, queries):
    result = []
    
    for s, e, k in queries:
        li = [arr[i] for i in range(s, e + 1) if arr[i] > k]  
        result.append(min(li) if li else -1)  
        
    return result
