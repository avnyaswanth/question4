# 1st ques recursive method 

x = int(input("Enter x value"))
n = int(input("Enter n value"))

def evaluate(x,n,ans = 0):
    if n == 0:
        return 0
    ans += 1/(x**n)+evaluate(x,n-1,ans)
    return ans

ans  = 0
print(evaluate(x,n,ans))