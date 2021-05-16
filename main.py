data = [int(n) for n in input()]


def compute(i, arr):
    if i == 0:
        return arr[0]
    result = 0
    for j in range(0, i+1):
        result += arr[j]
    return result


out = [compute(i, data) for i, _ in enumerate(data)]

print(out)
