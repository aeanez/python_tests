import numpy as np
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)

print(arr_2d[0][0])
print(arr_2d[0])

print(arr_2d[2, 1])

print(arr_2d[:2, 1:])
print(arr_2d[:2])
print(arr_2d[:, 1:])


print(arr_2d[:2, :2])
print(arr_2d[:2, 1:])
print(arr_2d[1:, :2])
print(arr_2d[1:, 1:])


print(arr_2d[:1, :1])
print(arr_2d[:1, 2:])
print(arr_2d[2:, :1])
print(arr_2d[2:, 2:])

print(arr_2d[1:2, 1:2])
