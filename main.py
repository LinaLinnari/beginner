data = [int(n) for n in input()]


out = [sum(data[0:i+1]) for i, _ in enumerate(data)]

print(out)
