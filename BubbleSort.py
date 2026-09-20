import math
# we are amiming to use divide and conquer to solve the mcs(maximum contious sum) problem in this list
A_list = []
# input of the list
while True:
    x = input("Enter an integer for the A_list (or q to stop): ")

    if x == "q":
        break

    A_list.append(int(x))

def bubbleSort(A):
    n = len(A)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # compare the big or small
            if A[j] > A[j + 1]:
                #swap the element
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                print("each inner loop: ", A)
        print("each outerloop: ", A)
    return A

A_sort = bubbleSort(A_list)
print("sorting result: ", A_sort)

def bubbleReverseSort(B):
    n = len(B)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # compare the big or small
            if B[j] < B[j + 1]:
                #swap the element
                temp = B[j]
                B[j] = B[j+1]
                B[j+1] = temp
                print("each inner loop: ", B)
        print("each outerloop: ", B)
    return B

B_sort = bubbleReverseSort(A_list)
print("Reverse sorting result: ", B_sort)

