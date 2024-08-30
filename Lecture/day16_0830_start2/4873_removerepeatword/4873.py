import sys
sys.stdin = open("input.txt", "r")

def find_continue_word(string):
    # 받은 string 잘라서 재귀 시킴
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            string = string[:i] + string[i + 2:]
            return find_continue_word(string)
    return string

T = int(input())
for test_case in range(1, T + 1):
    string = list(input())
    print(f'#{test_case} {len(find_continue_word(string))}')