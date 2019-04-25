import numpy as np
arr = np.arange(0, 11)

# saves boolean data for every array elemet comparison
bool_arr = arr > 5
print(bool_arr)

# we can get the values from the original array
# if they match with true bool_array elements
print(arr[bool_arr])

# prints numbers inside the array if they match
# the condition
# is the same example above but in one line
print(arr[arr < 3])
