def collatz(n):
    if n == 1:                             
        result = [1]
    elif n % 2 == 0:
        result = collatz(n // 2) + [n]
    elif n % 2 == 1:
        result = collatz((3 * n) + 1) + [n]
    return result


import pandas as pd
arr = []
for a in range (1,10):
    arr.append(len(collatz(a)))

df = pd.DataFrame(arr)

print(df)
print((df.describe()))
print(df.quantile(q = 0.5).iloc[0])