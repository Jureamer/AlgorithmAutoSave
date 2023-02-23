def solution(begin, end):
    answer = []
    MAX = 10000000
    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
            continue
        else:
            block = 1
            for i in range(2, int(num ** 0.5) + 1):
                if num != i and num % i == 0:
                    if num // i <= MAX:
                        block = num // i
                        break
                    else:
                        block = i
            
            answer.append(block)
    return answer