def solution(n):
    if 1<= n <= 100:
        if n % 2!= 0:
            return sum(i for i in range(1, n+1, 2))
        else:
            return sum(i**2 for i in range(0,n+1,2))
            
                