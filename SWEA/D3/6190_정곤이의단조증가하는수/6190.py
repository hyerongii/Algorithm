import sys
sys.stdin = open("input.txt", "r")

# 서로 곱한 수들 중에 그 중 최대 값 구하기
# 테스트 케이스가 낚았음... 70은 단조 증가하는 수가 아님
# 단조증가하는지 체크하는 함수
# 받은숫자 str으로 쪼개고 다시 숫자로 변환해 단조증가인지 확인하기
def is_minorincrease(num):
    c_num = list(str(num))
    # 한자리 수 이면 o
    if len(c_num) == 1:
        return True
    # 두자리 수 이상이면 체크
    else:
        count = 0
        for i in range(len(c_num) - 1):
            if c_num[i] <= c_num[i + 1]:
                count += 1
        if count == len(c_num) - 1:
            return True
        return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    # 단조증가 곱한 수 저장할 리스트 생성
    m_lst = []
    # 돌아가면서 값 다 곱해주자! 두개씩 묶을 수 있는 경우 다 고려
    for i in range(N-1):
        for j in range(i+1, N):
            # 단조증가하면 리스트에 넣어주고 아니면 말기
            if is_minorincrease(A[i] * A[j]):
                m_lst.append(A[i] * A[j])
    # 단조증가수만 모인 리스트에서 가장 큰 값 찾기
    if len(m_lst):
        print(f'#{tc} {max(m_lst)}')
    else:
        print(f'#{tc} -1')


