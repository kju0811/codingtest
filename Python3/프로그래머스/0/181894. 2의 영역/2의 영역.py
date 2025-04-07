def solution(arr):
    # 모든 2의 위치 찾기
    indices = [i for i, num in enumerate(arr) if num == 2]
    
    # 2가 없는 경우
    if not indices:
        return [-1]
    
    # 첫 번째와 마지막 2의 위치로 슬라이싱
    start = indices[0]
    end = indices[-1]
    return arr[start:end+1]