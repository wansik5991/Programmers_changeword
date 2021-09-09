import numpy as np

def solution(begin, target, words):

    words[1:] = words
    words[0] = begin
    relation = list(np.zeros(len(words)**2).reshape(-1,len(words)))

    for i in range(len(words)) :
        for j in range(i+1, len(words)) :
            cnt = 0
            for k in range(len(begin)) :
                if words[i][k] != words[j][k] :
                    cnt += 1
            if cnt <= 1 :
                relation[i][j] = 1
                relation[j][i] = 1
    
    check = [False for _ in range(len(words)+1)]
    steps = [99 for _ in range(len(words))]

    def bfs(index, step) :
        check[index] = True
        steps[index] = step
        for i in range(len(words)) :
            if relation[index][i] == 1 and steps[i] > step :
                bfs(i, step + 1)

    bfs(0, 0)

    try :
        target = words.index(target)
    except ValueError :
        target = 0 
    finally :
        return steps[target] if target != 0 else 0

print(solution("hit", "hit",["hit", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log"]))