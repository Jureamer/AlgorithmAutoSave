import sys
n = int(input())
arr = [list(input()) for _ in range(n)]
global answer
answer = ""

def divide(tree, paren):
    global answer
    
    length = len(tree)
    mark = tree[0][0]
    if length == 1:
        answer += mark
        return

    canComp = True
    
    for i in range(length):
        for j in range(length):
            if mark != tree[i][j]:
                canComp = False
                answer += "("
                divide([row[:length//2] for row in tree[:length//2]], "")
                divide([row[length//2:]for row in tree[:length//2]], "")
                divide([row[:length//2]for row in tree[length//2:]], "")
                divide([row[length//2:]for row in tree[length//2:]], "")
                answer += ")"
                return
            
    if canComp:
        answer += mark
        return
    
divide(arr, "")
print(answer)