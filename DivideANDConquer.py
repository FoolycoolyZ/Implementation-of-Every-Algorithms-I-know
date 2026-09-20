import math
# we are amiming to use divide and conquer to solve the mcs(maximum contious sum) problem in this list
A_list = []
# input of the list
while True:
    x = input("Enter an integer for the A_list (or q to stop): ")

    if x == "q":
        break

    A_list.append(int(x))

def mcs(A_list, L, R):
    # Base case
    if(L == R):
        return A_list[L]
    else:
        C = math.floor((L + R) / 2)
        # Divide the list
        Lmax = mcs(A_list, L, C)
        Rmax = mcs(A_list, C + 1, R)

        # Left part of the straddle maximum
        LSsum = 0
        LSmax = A_list[C]

        for i in range(C, L - 1, -1):
            LSsum += A_list[i]

            if LSsum > LSmax:
                LSmax = LSsum

        # Right part of the straddle maximum
        RSsum = 0
        RSmax = A_list[C + 1]

        for i in range(C + 1, R + 1):
            RSsum += A_list[i]

            if RSsum > RSmax:
                RSmax = RSsum

        # Straddle maximum
        Smax = LSmax + RSmax

        # Return the maximum of the three possibilities
        return max(Lmax, Rmax, Smax)


# Run MCS
if len(A_list) > 0:
    answer = mcs(A_list, 0, len(A_list) - 1)
    print("Maximum contiguous sum:", answer)   
