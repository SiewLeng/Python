def fn(series):
    series [-1] = series [-1] + 2

x = [1, 2, 3]
fn(x)
print('x after function call: ', x)