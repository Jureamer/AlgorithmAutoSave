'''
ababababa
aba

'''
doc = input()
word = input()

length = len(word)
answer = 0
idx = 0

while idx < len(doc):
    if doc[idx: idx+length] == word:
        answer += 1
        idx += length        
        continue
    idx += 1
    
print(answer)
    