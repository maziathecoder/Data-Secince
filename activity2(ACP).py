import numpy as np

arr = np.linspace(0, 9, 10, dtype=int)
print("Original Array:")
print(arr)

new_arr = arr.copy()
new_arr[new_arr % 2 == 1] = -1
print("\nArray with odd numbers replaced by -1:")
print(new_arr)

arr_2d = arr.reshape(2, 5)
print("\n2-D Array (2 rows):")
print(arr_2d)

even_sum = np.sum(arr[arr % 2 == 0])
print("\nSum of all even numbers:")
print(even_sum)