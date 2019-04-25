import numpy as np

arr = np.arange(0, 11)  # Generate an Array from 0 to 10 inclusive
print(arr)

print(arr[8])  # this shows the value in 8 position
print(arr[1:5])  # this shows values from 1 inclusive to 5 inclusive
print(arr[0:5])  # This shows values from 0 inclusive to 5 inclusive
print(arr[:6])  # prints from first element to sixth element
print(arr[5:])  # prints from fifth element and fordward

arr[0:5] = 100  # Changes values to 100 every index from 0 to 5
print(arr)

arr = np.arange(0, 11)  # Generate an Array from 0 to 10 inclusive
print(arr)

# This not really copy the array segment
slice_of_arr = arr[0:6]  #
print(slice_of_arr)

# if we try to change the value from this slice array
slice_of_arr[:] = 88
print(slice_of_arr)
# it will change the values from the original,
# so this array isnt a copy
print(arr)

# if you want to copy an array you can use the copy method
arr_copy = arr.copy()
arr_copy[:] = 60
print(arr)
print(arr_copy)
