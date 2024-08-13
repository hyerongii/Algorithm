import sys
sys.stdin = open("input.txt", "r")

dict = {"}":"{", ")":"("}

def matchingbracket(arr):
    stack = []

    for c in arr:
        if c in dict.values():
            stack.append(c)
        elif c in dict.keys():
            if len(stack) == 0 or stack[-1] != dict[c]:
                return 0
            
            stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    arr = input()
    print(f'#{tc} {matchingbracket(arr)}')