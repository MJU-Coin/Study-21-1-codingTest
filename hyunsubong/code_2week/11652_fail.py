# 카드

# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	256 MB	18663	5096	3820	28.002%

# 문제
# 준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.

# 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

# 입력
# 첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.

# 출력
# 첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.

import sys

num = int(sys.stdin.readline())
l = []
for i in range(num):
    l.append(int(sys.stdin.readline()))
top = 0
temp = 0
for i in l:
    count = l.count(i)
    if count > temp:
        top = i
        temp = count
    elif count == temp:
        if i < top:
            top = i
    else:
        continue
sys.stdout.write(str(top))