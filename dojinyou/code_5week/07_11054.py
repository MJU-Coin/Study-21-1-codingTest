# https://www.acmicpc.net/problem/11054

from sys import stdin
input = stdin.readline

n = int(input())
num = [0]
num.extend(list(map(int,input().split())))
dp = [[1,1] for _ in range(n+1)]
maxValue = 1
for i in range(2,n+1):
    for j in range(1,i):
        if (num[j] < num[i]) and (dp[j][0]+1 > dp[i][0]) :
            dp[i][0] = dp[j][0]+1
        if (num[j] > num[i]) and (max(dp[j][0],dp[j][1])+1 > dp[i][1]) :
            dp[i][1] = max(dp[j][0],dp[j][1])+1
    maxValue = max(maxValue, dp[i][0], dp[i][1])
print(maxValue)