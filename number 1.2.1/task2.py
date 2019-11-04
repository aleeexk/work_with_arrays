import numpy as np

with open("data.txt") as f:
    for line in f:
        arr = np.array([float(x) for x in line.split()])


arr.sort()
print(arr)
print(arr.min())
print(arr.max())
print(arr.mean())
print(((arr - arr.mean()) ** 5).mean())
print(np.std(arr).round(3))

complexarr = tuple(np.genfromtxt('complex.txt', delimiter='\n', dtype=complex))
print('Absolute sorting:', str(sorted(complexarr, key=lambda x: abs(x))))
print('Reverse real sorting:', str(sorted(complexarr, key=lambda x: x.real, reverse=True)))

stringarr = tuple(np.genfromtxt('string.txt', delimiter=' ', dtype=str))
print('Lenght sorting:', str(sorted(stringarr, key=lambda x: len(x))))
print('Lexical and graphic order sorting:', str(sorted(stringarr)))
