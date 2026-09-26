import math
# we are amiming to use divide and conquer to solve the mcs(maximum contious sum) problem in this list
A_list = []
# input of the list
while True:
    x = input("Enter an integer for the A_list (or q to stop): ")

    if x == "q":
        break

    A_list.append(int(x))

def mcs_brute_force(A):
    max_sum = A[0]

    for i in range(len(A)):
        current_sum = 0

        for j in range(i, len(A)):
            current_sum += A[j]

            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


print(mcs_brute_force(A_list))
