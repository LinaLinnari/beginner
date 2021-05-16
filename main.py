data = [1, 2, 3, 4, 1]

out = [data[i] if i == 0 else data[i - 1] + data[i] for i, _ in enumerate(data)]

print (out)
