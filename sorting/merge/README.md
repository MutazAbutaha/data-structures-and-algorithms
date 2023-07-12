# Merge Sort :
The mergesort function takes an array as input.

It checks the length of the array, and if it's greater than 1:

It calculates the midpoint mid of the array.

It divides the array into two halves:

left (from index 0 to mid-1)

right (from index mid to the end).

It recursively calls mergesort on the left half and right half.

Finally, it merges the sorted left and right halves using the merge function.

Merge:

The merge function takes three arrays as input: left, right, and arr.

It initializes three pointers i, j, and k to keep track of the indices in left, right, and arr, respectively.

It compares elements from left and right arrays and places the smaller element in arr at index k.

The pointers i, j, and k are updated accordingly.

After the above loop, if there are any remaining elements in either left or right array, they are appended to arr.

```python
        [4, 2, 1, 5, 3]             # Initial unsorted array
               /    \
     [4, 2]           [1, 5, 3]     # Splitting into halves
    /     \          /     \
  [4]     [2]      [1]     [5, 3]   # Splitting further
   |       |       |     /    \
  [2, 4]  [1]     [1, 3] [5]        # Merging back sorted halves
       \     /           \
     [1, 2, 4]         [1, 3, 5]    # Final merge of left and right halves
          \               /
       [1, 1, 2, 3, 4, 5]          # Sorted array

```

### Time Complexity:
The time complexity : O(n log n) 

### Space Complexity:
The space complexity :  O(n)