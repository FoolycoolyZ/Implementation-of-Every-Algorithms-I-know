import math
# we are amiming to use divide and conquer to solve the mcs(maximum contious sum) problem in this list
A_list = []
# input of the list
while True:
    x = input("Enter an integer for the A_list (or q to stop): ")

    if x == "q":
        break

    A_list.append(int(x))

# We are going to start selection sort 
def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        minindex = i 
        for j in range(i+1, n):
            if A[j] < A[minindex]:
                minindex = j
        A[i], A[minindex] = A[minindex], A[i]
    return A
A_sort = selectionSort(A_list)
print("The Sorted list is: ", A_sort)

