def dfs(current, arr, visited, path):
    path.append(current)            # 방문경로 추가

    # index 탐색
    for i in range(len(arr)):
        if arr[i][0] == current and i not in visited:
            visited.append(i)
            dfs(arr[i][1], arr, visited, path)
    else:
        return


# 알파벳 순서대로 정렬하고 시작하자!
def solution(tickets):
    tickets.sort(key=lambda x: x[1])      # 도착지를 알파벳 순으로 정렬하기

    path = [] # 여기에 방문한 도시 넣어주자
    visited = [] # 여기에 이미 방문한 인덱스 넣어주기

    dfs("ICN", tickets, visited, path)

    answer = path
    return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "AAA"], ["DDD", "ICN"], ["ICN", "DDD"]]
print(solution(tickets))