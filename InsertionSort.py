import math
# we are amiming to use divide and conquer to solve the mcs(maximum contious sum) problem in this list
A_list = []
# input of the list
while True:
    x = input("Enter an integer for the A_list (or q to stop): ")

    if x == "q":
        break

    A_list.append(int(x))

def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while(j >= 0 and key < A[j]):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key 
    return A

print(insertionSort(A_list))
