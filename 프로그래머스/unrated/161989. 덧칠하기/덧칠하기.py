def solution(n, m, section):
    answer = 0
    section.sort()
    idx = 0
    color_distance = 0
    
    while idx < len(section):
        # print(f'idx: {idx}, color_distance: {color_distance}, answer: {answer}')
        if section[idx] > color_distance:
            color_distance = section[idx] + m - 1
            idx += 1
            answer += 1
            continue
        
        idx += 1
    return answer