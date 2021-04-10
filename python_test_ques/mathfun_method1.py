# 1st ques method 1

x = int(input("Enter x value"))
n = int(input("Enter n value"))

ans = 0
for i in range(1,n+1):
    ans += 1/(x**i)

print(ans)