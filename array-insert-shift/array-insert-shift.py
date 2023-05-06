import math

arr = [1, 2, 3, 4, 5, 6, 7]
n = 50

def insert_Shift_Array(arr, n):
    mid = math.ceil((len(arr) / 2))
    new_array = arr[:mid] + [n] + arr[mid:]
    return new_array
print(insert_Shift_Array(arr, n))