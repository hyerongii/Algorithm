from collections import deque
def solution(begin, target, words):

    if target not in words:         # 타겟이 words 안에 없을때 0 반환
        return 0

    q = deque()
    q.append(begin)
    cnt = 0
    visited = [False] * len(words)

    while q:
        char = q.popleft()

        if char == target:
            return cnt

        # 타겟과 문자 하나만 틀린경우 반환
        s = 0
        for i in range(len(target)):
            if target[i] == char[i]:
                s += 1
        if s == len(target) - 1:
            return cnt+1

        # words 에서 돌기
        for idx, word in enumerate(words):

            # 이미 방문한거 세지 x
            if visited[idx]:
                continue

            same = 0
            for i in range(len(word)):
                if word[i] == char[i]:
                    same += 1
            if same == len(word)-1:
                q.append(word)
                visited[idx] = True
                cnt += 1
                break

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

