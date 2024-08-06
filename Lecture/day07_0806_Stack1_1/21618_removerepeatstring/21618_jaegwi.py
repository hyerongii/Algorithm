import sys
sys.stdin = open("input.txt", "r")

def find_continue_word(string):
    
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
        # 연속으로 들어온다면 remove
            string = string[:i] + string[i+2:]
            return find_continue_word(string)

    return string

T = int(input())
for test_case in range(1, T + 1):
    # 입력문자 수정해야하기 때문에,, list로 변환
    string = list(input())
    print(f'#{test_case} {len(find_continue_word(string))}')
