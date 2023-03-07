def solution(m, musicinfos):
    answer = []
    
    for music in musicinfos:
        start, end, title, melody = music.split(",")
        startTime = 0
        endTime = 0
        
        # 시간 변환
        for i in range(2):
            if i == 0:    
                startTime += int(start.split(":")[0]) * 60
                endTime += int(end.split(":")[0]) * 60
                continue
            
            startTime += int(start.split(":")[1])
            endTime += int(end.split(":")[1])
        
        playTime = endTime - startTime
        
        # 멜로디 # 처리 변환
        convertM = ""
        convertMelody = "" 
        for i in range(len(m)):
            if i == len(m) - 1:
                if m[i] != "#":
                    convertM += m[i]
                break
            
            if m[i+1] == "#":
                convertM += m[i].lower()
                continue
            
            elif m[i] != "#":
                convertM += m[i]
                continue
            
        for i in range(len(melody)):    
            if i == len(melody) - 1:
                if melody[i] != "#":
                    convertMelody += melody[i]
                break
            
            if melody[i+1] == "#":
                convertMelody += melody[i].lower()
                continue
            
            elif melody[i] != "#":
                convertMelody += melody[i]
                continue
                
        
        # 음악 길이에 따른 멜로디 조정
        if playTime > len(convertMelody):
            convertMelody = convertMelody * (playTime // len(convertMelody)) + convertMelody[:playTime % len(convertMelody)]
        
        if playTime < len(convertMelody):
            convertMelody = convertMelody[:playTime]
            
        # 멜로디 찾기
        if convertM in convertMelody:
            answer.append((playTime, title))
            continue
    # print(f'answer: {sorted(answer, key=lambda x: x[0], reverse=True)[0][1]}')
    return sorted(answer, key=lambda x: x[0], reverse=True)[0][1] if answer else "(None)"