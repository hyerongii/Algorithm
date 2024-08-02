import sys
sys.stdin = open("GNS_test_input.txt", "r")

string = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc, N  = input().split()
    N = int(N)
    input_arr = list(input().split())
    
    # 내가 푼 방법
    # 숫자로 변환
    for i in range(N):
        input_arr[i] = string.index(input_arr[i])

    # 그리고 정렬
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if input_arr[j] > input_arr[j+1]:
                input_arr[j], input_arr[j+1] = input_arr[j+1], input_arr[j]
    
    # 그리고 다시 str 로 변환
    for i in range(N):
        input_arr[i] = string[input_arr[i]]

    print(tc)
    print(*input_arr)


    # 1 방법
    '''
    string 변수를 앞에서 부터 순회를 한다.
    ZRO -> 
    words 를 한바퀴 돌면서 ZRO에 해당하는 친구들을 결과 값에 추가
    ONE -> 
    words를 한 바퀴 돌면서 ONE에 해당하는 친구들을 결과 값에 추가
    .. string을 돌면 정렬 완료한 문자열을 구할 수 있음
    '''
    # 2 방법
    '''
    nlogn -> sort()의 시간복잡도
    문자에서 숫자로 변환 후에 새로운 리스트에 추가한다.
    정렬 후 숫자로 문자로 다시 변환함
    '''
    # 3 방법
    '''
    카운팅 하고 그냥 그 str을 카운팅 개수만큼 출력하기 -> 카운팅 정렬 시간 복잡도 n+k
    string의 인덱스에 count_list 값에 저장함

    max_value = 9  # 인텍스 최대 값

    count_list = [0]*(max_value + 1)

    for word in input_arr:
        count_list[string딕셔너리[word]] += 1

    result = []
    for i, c in enumerate(count_list):
        result.extend([string[i]]*c)
    print("".join(result))
    '''

