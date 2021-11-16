# smallest-impossible-sum-of-2-elements-in-an-array
Given an array of size N, find the smallest positive integer value that cannot be represented as sum of some elements from the array.

Step 0 : Initialisation

Other than ’N’  that holds the size of elements present in array ‘array’, a min_sum and sum_array are also initialised.
sum_array will be used immidiately for holding a compilation of all the possible sums of any two elements, or already existing elements. 
And min_sum will be used in the final step to store the minimum possible sum that is to present in the sum_array.

Step 1 :  Create sum_array

This step will create a compilation of all the possible sums of any two elements, or already existing elements. 

The approach to fulfil this is as follows : 
Any element is to be considered separately first and then a inside a loop, all elements following a current element are added together and recorded in sum_array. 
The last element however will not be traversed (except for taking it individually in sum_element) in order to minimise the repeated additions.

This approach is simple however the resultant array is unsorted. 
Not to mention the size of it.
This takes us to our next step of sorting our array.

Step 2 : Sorting Sum_array

Sum_array is the array that holds no repeated values but is still longer than a traditional array, as such one must take space and time complexity in mind. 
Here I have applied merge sort to simplify this. However this part takes a majority of the code lines. 
One may chose to swap it for a smaller lines of code.

First step in this process is to separate the sum_aray into halves recursively and sort them accordingly. 
Here, separation is done by the function ‘separate’.
It only takes that array as its argument and consequently calls upon ‘re_arrange’ function to start the actual sorting.

In re_arrage function, a temporary array is used to store the sorted version of two already sorted arrays and returns it. 
It takes 2 arrays as its arguments and uses index1 and index2 respectively for traversing them.

In a conjoined loop of traversing both arrays together only the smaller elements are added to the resultant sorted array and 
any of the remaining elements (that could not be traversed together because we ran out of 1 of the two arrays) are added at the end. 
This is because all the remaining elements would be sorted and larger.

Step 3 : Finding the minimum impossible sum of elements.

Note : this value cannot be one that is already in the given array, which is why those values were also included the the sum_array.

This step can be better understood with a example : 

Example :
Array = [ 1, 2, 5 ]
sum_array = [ 1, 2, 3, 5, 6, 7 ]
                      |
                      \/         
                The gap is here

In this example the answer to our problem would be the one that we didn’t find in the sum array.
Meaning there is a sudden gap in our array.
We need to find that missing element.
So we return the index of that element where we suddenly find a gap and increment it by 1. 
This is because indexes start from 0 and sums from 1 as there are no negative value in the given array.

Once we have found our missing element we can stop.
