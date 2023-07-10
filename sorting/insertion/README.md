## Insertion Sort

The insert function takes a sorted array (sorted_array) and a value to be inserted (value).

Initialize i to 0.
Iterate while i is less than the length of sorted_array and value is greater than the element at index i in sorted_array.
Increment i by 1 until the condition is no longer satisfied.
Insert value at index i in sorted_array.
Visualization:

insert([1, 3, 5, 7], 4)
Initial State: [1, 3, 5, 7]

Iteration 1: i = 0
Condition (4 > 1) is true. Incrementing i.

Iteration 2: i = 1
Condition (4 > 3) is true. Incrementing i.

Inserting 4 at index 2.

Final State: [1, 3, 4, 5, 7]
Insertion Sort Algorithm Visualization:

The insertion_sort function takes an input array (input) and applies the insertion sort algorithm to sort the array.

Create an empty sorted array and add the first element of input to it.
Iterate over the remaining elements of input from index 1 to the end.
For each element, call the insert function to insert it into the sorted array at the correct position.
Return the sorted array as the sorted result.
Visualization:

insertion_sort([5, 2, 4, 6, 1, 3])
Initial State: input = [5, 2, 4, 6, 1, 3], sorted = [5]

Iteration 1: Inserting 2 into sorted.
Intermediate sorted state: [2, 5]

Iteration 2: Inserting 4 into sorted.
Intermediate sorted state: [2, 4, 5]

Iteration 3: Inserting 6 into sorted.
Intermediate sorted state: [2, 4, 5, 6]

Iteration 4: Inserting 1 into sorted.
Intermediate sorted state: [1, 2, 4, 5, 6]

Iteration 5: Inserting 3 into sorted.
Intermediate sorted state: [1, 2, 3, 4, 5, 6]

Final sorted state: [1, 2, 3, 4, 5, 6]


## Efficency

Time: 
insert O(n)
insert_sort o(n^2)

Space: 
insert O(1)
insert_sort O(n)
