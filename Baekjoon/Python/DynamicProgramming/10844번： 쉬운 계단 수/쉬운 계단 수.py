#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10844                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10844                          #+#        #+#      #+#     #
#    Solved: 2024/05/30 15:30:11 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
    1   2   3   4   5   ... n-1 n
0   0   1   1   3   ...
1   1   1   3   4   ...
2   1   2   3   7   ...
3   1   2   4   7   ...
4   1   2   4   8   ...
5   1   2   4   8   ...
6   1   2   4   8   ...
7   1   2   4   7   ...
8   1   2   3   6   ...
9   1   1   2   3   ...
    9   17  32  61  ...
'''
import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(n)] * 10
for i in range(1, 10):
    dp[0][i] = 1    # n=1 경우, 0 제외 1카운트

for i in range(1, n):   # 자릿수
    for j in range(10): # 0~9
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n-1]) % 1000000000)