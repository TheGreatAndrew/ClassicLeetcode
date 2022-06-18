### leetcode random
# prefix sum : is when i is sum of all previous index i-1,i-2,...
# https://leetcode.com/problems/k-closest-points-to-origin/discuss/1578232/All-possible-3-Python-solutions-%2B-interviewer-expectations heap, quick select


### rebind
# assign (in other languages) : assign 5 to variable a -> variable b is a different box
# name/ identifier (in Python) : variable a, b bound to same object. can reassign
# assign : var will refer to another object value. assignment never copies value
# assign/ binding/ reassign/ rebinding
# Immutable values : numbers, strings, and tuples -> it doesn’t change, it creates a new value 
# Mutable : the rest, including lists, dicts, and user-defined objects
# assignment for immutable values will return new value, so there won't be any surprise


### function 
# default paramter values -> function default value is evaluated at function definition time, not everytime you call a function -> solution is to create initial value inside function at runtime
# argument are passed by assignment
    # mutable : can mutate, can rebind but not outer scope
    # immutable : can rebind but not outer scope  


### 4 collection data types
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


### lambda 
# lambda : small anonymous function 


#### WERID CODE
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/64963/3-lines-with-O(1)-space-1-Liners-Alternatives
root = (root.left, root.right)[p.val > root.val]

# check if any items in the list is True
mylist = [False, True, False]
x = any(mylist)

# operators
print(5/2 == 2.5)
print(5//2 == 2)
print(5)  






##### BITE 
# x, y = oldX, oldY
    # no need for holder 

# * asterisk 
# is multiply list, unpacking list, *args for any arguments
 
# queue = collections.deque([(root)])
# queue = collections.deque()
# queue.append(root)

#### SPEED
# https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated set is faster and itertools



