import sys
sys.stdin = open("input.txt", "r")

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
                return -1

            stack.pop()
    
    if len(stack) == 0:
        return 1
    return -1

match_dict = {")":"("}

T = int(input())
for tc in range(1, T+1):
    string = input()
    # stack = []
    # result = 0

    # for char in string:
    #     if char in match_dict.values():
    #         stack.append(char)
    #     elif char in match_dict.keys():
    #         if (len(stack) == 0) or stack[-1] != match_dict[char]:
    #             result = -1
    #             print(f'#{tc} {result}')
    #             break

    #         stack.pop()
            
    # if len(stack) == 0:
    #     result = 1
    # else:
    #     result = -1      

    print(f'#{tc} {is_bracket_match(string)}')