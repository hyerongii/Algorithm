import sys
sys.stdin = open("input.txt", "r")

grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

T = int(input())
for tc in range(1, T+1):
    # N: 학생 수(항상 10의 배수;;), K: 학점 알고싶은 학생의 번호
    N, K = map(int, input().split())
    # 총점 리스트
    score_lst = []
    # N줄 만큼 학생의 점수 각각 들어옴. 중간, 기말, 과제 순으로
    # 총점 바로 계산해서 리스트에 넣어주자
    for i in range(1, N+1):
        mid, fin, hw = map(int, input().split())
        # i는 학생 번호, 총점 리스트로 묶어서 리스트에 같이 저장해주기
        score = [i, (mid*0.35) + (fin*0.45) + (hw*0.2)]
        score_lst.append(score)
    # 점수 기준으로 정렬해주기 -> sort / key 기능 활용해보기
    score_lst.sort(key=lambda x: x[1], reverse=True)
    # 학점 부여 하기 N의 몫 만큼 잘라서 grade 부여하고 넘어가야함
    # 여기가 제일 빡셋다 ㅠㅠ
    for j in range(N):
        if j % (N//10) == 0:
            # N이 10의 2배수라면 2번 반복
            for k in range(N//10):
                # grade 인덱스 찾기 위해 다시 배수로 나눠주기
                score_lst[j+k].append(grade[j//(N//10)])
    # 학점 알고싶은 학생의 번호 대입해 학점 출력
    for data in score_lst:
        if data[0] == K:
            print(f'#{tc} {data[2]}')


