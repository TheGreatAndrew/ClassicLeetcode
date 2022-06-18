# https://www.geeksforgeeks.org/analysis-of-different-sorting-techniques/ remember this
# buble sort, insertion sort -> worst O(n^2) when array is reversed sorted 
# selection sort -> all O(n^2)
# merge sort -> all O(nlogn), but space is n
# heap sort -> all O(nlogn)
# quick sort (divide conquer) -> 
# radix sort -> nk
# count sort -> n+k
# bucket sort -> best n+k, worst nk if all elements n same bucket 


# prepare mergesort, quicksort, insertionsort


# quicksort
# pick pivot random (but avoid first or last element), then left pointer-right pointer compare and switch place. then compare [0, pivot] [pivot, n]
# O(nlogn) go through n element, with logn swap
