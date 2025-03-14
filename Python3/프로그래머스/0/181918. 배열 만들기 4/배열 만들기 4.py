def solution(arr):
    stk = []
    i = 0
    if 1<= len(arr) <= 100000 and all(1<= i <=100000 for i in arr):
        while i < len(arr):
            if not stk:
                stk.append(arr[i])
                i+=1
            elif stk and stk[-1] < arr[i]:
                stk.append(arr[i])
                i+=1
            elif stk and stk[-1] >= arr[i]:
                stk.pop()
        return stk