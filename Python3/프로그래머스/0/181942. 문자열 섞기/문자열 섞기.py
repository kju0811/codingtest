def solution(str1, str2):
    answer = ''
    if 1<= len(str1)==len(str2)<=10:
        for i in range(0,len(str1)):
            answer = answer + str1[i] + str2[i]
        return answer
         