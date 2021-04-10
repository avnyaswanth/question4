# 2nd ques

n = int(input("Enter n value"))

def find_next_in_series(n):
    if n % 2 == 0:
        return (n*n - 1)
    else:
        return (n*n + 1)

print(find_next_in_series(n))