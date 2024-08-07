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

    result = []
    # 리스트 내 돌면서 date계산하기 
    for i in range(N):
        # 이때, 나머지가 0 이 아니면 몫보다 +1 해줘서 날짜수 확실히 해줌
        if (100-progresses[i])%speeds[i] != 0:
            date = ((100-progresses[i])//speeds[i])+1
        else:
            date = ((100-progresses[i])//speeds[i])
        """
        from math import ceil
        date = ceil((100 - progresses[i]) / speeds[i])
        25 ~ 28 line 은 위의 ceil 함수를 사용해서 구현할 수 있습니당 
        
        그리고 progresses[i]는 자주 사용하기 때문에 변수로 지정해서 변수로 활용해주면 좋습니다.
        progress = progress[i] 로 놓고, progress를 사용 
        """
        # 그리고 그 date를 stack에 쌓는데, 
        # 큰 date 뒤에 작은 date가 들어오면 큰 date 값으로 변환해 쌓아줌
        if not stack or stack[-1] < date:
            stack.append(date)
        elif stack[-1] >= date:
            stack.append(stack[-1])
        """
        위에 40 ~ 43 line을 아래와 같이 바꾸면, 밑에서 각 작업 번호가 몇 개 나오는 지 세지 않아도 됩니다. 
        결국 같은 원리로 동작하는건데, 작업속도가 더 빠르면 누적 작업개수를 저장하는 리스트를 만들어서 누적시켜주는 원리입니다.
        텍스트로 설명하기 애매한데 아래 코드 보고 이해 안되면 말씀주세요! 여튼 아래처럼 하면 count하는 부분을 안해도 됩니다.
        물론 원래 작성하셨던 코드도 충분히 훌륭해서, 굳이 개선하자면 아래와같아지는 것 뿐이니까 그냥 참고로만 받아드리시면 됩니다~
        어려운 문젠데 잘 푸셨네요~ 고생하셨어요
        
        if not stack or stack[-1] < date:
            stack.append(date)
            result.append(1)
        elif stack[-1] >= date:
            result[-1] += 1
        """
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
