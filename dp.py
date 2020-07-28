dp = [0 for i in range(100)]
dp[0], dp[1], dp[2], dp[3] = 0,1,2,4

for j in range(4,100):
    dp[j] = dp[j-1]+dp[j-2]+dp[j-3]

testing = int(input())
for i in range(testing):
    a = int(input())
    print(a)
