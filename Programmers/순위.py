'''
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다.
권투 경기는 1대1 방식으로 진행이 되고, 
만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 
심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 
하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 
정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

선수의 수는 1명 이상 100명 이하입니다.
경기 결과는 1개 이상 4,500개 이하입니다.
results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
모든 경기 결과에는 모순이 없습니다.
'''
def dfs(node, adjL, cnt):
    if not adjL[node]:
        return

    if cnt == n-1:
        return

    for i in adjL[node]:
        dfs(i, adjL, cnt + 1)


def solution(n, results):
    # 인접리스트 만들어주기, 0번은 없는거로 치자, 거꾸로
    adjL = [[] for _ in range(n+1)]

    for match in results:
        adjL[match[1]].append(match[0])     # 방향 1개임

    # 승리, 패배 한 숫자 더해서 자기 자신 제외한 만큼 일때 카운트 하기
    visited = [False] * (n+1)

    for node in range(1, n+1):
        dfs(node, adjL, 0, visited)

    answer = 0
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n, results))