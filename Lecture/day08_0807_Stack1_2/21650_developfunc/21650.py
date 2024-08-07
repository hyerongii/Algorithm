# test case
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

# 리스트 내 개수 세는 함수 
# 예: array: [5, 7, 7] n: 7 -> 2
def count_num(array, n):
    answer =0
    for i in array :
        if i ==n :
            answer+=1
    return answer

# 메인 함수
def solution(progresses, speeds):
    stack = []
    answer = []
    
    # 받은 리스트 요소의 개수
    N = len(progresses)
    
    # 리스트 내 돌면서 date계산하기 
    for i in range(N):
        # 이때, 나머지가 0 이 아니면 몫보다 +1 해줘서 날짜수 확실히 해줌
        if (100-progresses[i])%speeds[i] != 0:
            date = ((100-progresses[i])//speeds[i])+1
        else:
            date = ((100-progresses[i])//speeds[i])

        # 그리고 그 date를 stack에 쌓는데, 
        # 큰 date 뒤에 작은 date가 들어오면 큰 date 값으로 변환해 쌓아줌
        if not stack or stack[-1] < date:
            stack.append(date)
        elif stack[-1] >= date:
            stack.append(stack[-1])

    # 그렇게 쌓여진 스택 라스트를 검토 
    # 만약 date -> [5, 10, 1, 1, 20, 1]
    # stack -> [5, 10, 10, 10, 20, 20]

    # 그리고 answer에 세어준 값 넣어주기
    for i in stack:
        c = count_num(stack, i)
        answer.append(c)
        for _ in range(c-1):
            stack.remove(i)
    # answer -> [1, 3, 2]

    return answer

print(solution(progresses,speeds))
