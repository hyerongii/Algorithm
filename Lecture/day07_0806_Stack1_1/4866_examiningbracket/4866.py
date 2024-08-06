import sys
sys.stdin = open("input.txt", "r")

# 괄호 매칭하는 dict 생성
match_dict = {"}":"{", ")":"("}

def is_bracket_match(string):
    stack = []
    # 입력된 문자열의 문자중에
    for char in string:
        # 여는 괄호가 있다면
        if char in match_dict.values():
            # stack에 저장
            stack.append(char)
        # 닫는 괄호가 있다면
        elif char in match_dict.keys():
            # 스택이 비어있는지, 스택 마지막 괄호의 value랑 비교
            if (len(stack) == 0) or stack[-1] != match_dict[char]:
                return 0

            stack.pop()
    
    if len(stack) == 0:
        return 1
    return 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = input()
    print(f'#{test_case} {is_bracket_match(arr)}')

