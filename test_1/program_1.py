def fn(n, series):
            if n >= 5:
                series.append(n*n)
                n = n + 1
n = 5
lst=[ ]
fn(n,lst)
print('n >>>', n)
print('lst >>>', lst)