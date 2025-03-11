def solution(arr, queries):
    
    if 1<=len(arr)<=1000 and all(0<=i<=1000000 for i in arr) and 1<=len(queries)<=1000 and all( 0<= i<j<len(arr) for i,j in queries):
        for i in queries:
            arr[i[0]],arr[i[1]] = arr[i[1]],arr[i[0]]
        return arr