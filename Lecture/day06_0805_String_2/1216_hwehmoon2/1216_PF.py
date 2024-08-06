import sys
sys.stdin = open("input.txt", "r")

def finding_longest_palindrome(arr):

    # 가장 긴 회문의 글자 수를 저장할 변수
    max_len = 1 

    # 행 우선 탐색
    for i in range(N):
        # 길이 100, 99, 98 ... 까지의 윈도우 만들기 /// 긴 것 부터 만들기!!!
        for length in range(N, 1, -1):  
            # 시작좌표, 차례대로 자르기
            for start in range(N-length+1):
                # 회문인지 확인하는 함수 만들기
                if is_palindrome(arr[i][start:start + length]):
                    return length

                # 세로 방향 검사
                column = []
                for j in range(start, start + length):
                    column.append(arr[j][i])

                '''
                리스트 컴프리헨션 으로 제작도 가능!
                if is_palindrome([arr[j][i] for j in range(start, start+length)]):
                    return length
                '''

                if is_palindrome(column):
                    return length

def is_palindrome(string):
    
    left, right = 0, len(string) -1
    
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

for test_case in range(1, 11):
    tc = int(input())
    N = 100
    arr = [input() for _ in range(100)]

    result = finding_longest_palindrome(arr)

    print(f'#{test_case} {result}')

