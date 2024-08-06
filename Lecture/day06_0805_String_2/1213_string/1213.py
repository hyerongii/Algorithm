
import sys
sys.stdin = open("input.txt", "rt", encoding='UTF8')

def bruteforce(pattern, text):
    result = 0

    pattern_idx = 0
    compare_idx = 0

    while compare_idx < len(text):
        if text[compare_idx] != pattern[pattern_idx]:
            compare_idx = compare_idx - pattern_idx + 1
            pattern_idx = 0
            continue

        pattern_idx += 1
        compare_idx += 1

        if pattern_idx == len(pattern):
            result += 1
            pattern_idx = 0
            compare_idx = compare_idx - pattern_idx + 1
        
    return result

for _ in range(10):
    tc = int(input())
    
    pattern = input()
    text = input()

    print(f'#{tc} {bruteforce(pattern, text)}')

