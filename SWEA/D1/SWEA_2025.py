'''
2025. N줄 덧셈

1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
단, 주어질 숫자는 10000을 넘지 않는다.

[예제]
주어진 숫자가 10 일 경우 출력해야 할 정답은,
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
'''

# 1부터 주어진 숫자만큼 나열
# 그리고 모두 더하기

T = int(input())
sum = 0

# 1부터 주어진 숫자만큼 연달아 증가하면서 반복
for num in range(1, T+1):
    sum += num

print(sum)