def solution(arr, divisor):
    answer = []
    
    for i in sorted(arr):
        if i % divisor == 0:
            answer.append(i)
            
    if len(answer) > 0:
        return answer
    else:
        return [-1]