import math
# we are amiming to use divide and conquer to solve the mcs(maximum contious sum) problem in this list
A_list = []
# input of the list
while True:
    x = input("Enter an integer for the A_list (or q to stop): ")

    if x == "q":
        break

    A_list.append(int(x))

n = len(A_list)
def KadaneAlgorithm(A):
    maxoverall = A_list[0]
    maxendingat = A_list[0]
    for i in range (1, n):
        maxendingat = max(maxendingat + A[i], A[i])
        if(maxendingat > maxoverall):
            maxoverall = maxendingat
    return maxoverall

print("Maximum contiguous sum:", KadaneAlgorithm(A_list))
