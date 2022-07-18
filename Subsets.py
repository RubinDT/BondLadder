# from https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/

# class Subsets: # why can't I make this a class?
def subsetsUtil(A, subset, index):
    print(subset)
    all_subsets.append(subset.copy())
    for i in range(index, len(A)):
        # include the A[i] object in subset
        subset.append(A[i])

        # move onto the next element
        subsetsUtil(A, subset, i+1)

        # exclude the A[i] from subset and
        # triggers backtracking (?)
        subset.pop(-1)
    return

# this funciton returns the subsets of vector A
def subsets(A):
    subset = []

    # keep strack of current element in vector A
    index = 0
    subsetsUtil(A, subset, index)

# Driver code

array = [1,2,3]
all_subsets = []
subsets(array)
print(all_subsets)