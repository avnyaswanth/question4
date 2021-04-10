# 3rd ques

x = int(input("enter number"))
y = int(input("enter number"))
a = int(input("enter number"))
b = int(input("enter number"))

def solve(x,y,a,b):
    numerator = ((x + (1/y)) ** a) * ((x - (1/y)) ** b)
    denominator = ((y + (1/x)) ** a) * ((y - (1/x)) ** b)
    ans  = numerator/denominator
    return ans

print(solve(x,y,a,b))