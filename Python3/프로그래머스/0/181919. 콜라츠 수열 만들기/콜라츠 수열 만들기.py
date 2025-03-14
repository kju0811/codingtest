def solution(n):
    answer = [n]
    if 1<=n<=1000:
        while n != 1:
            if n%2==0:
                n//=2
            else:
                n = 3*n+1

            answer.append(n)
        return answer