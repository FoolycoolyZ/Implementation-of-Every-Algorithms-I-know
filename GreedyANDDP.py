import math
coins = []
# input of the list
while True:
    x = input("Enter an integer for the coinlist (or q to stop): ")

    if x == "q":
        break

    coins.append(int(x))

optimal_coins = coins[::-1]
#amount of the coin
amount = int(input("Enter the amount of the coin you want to exchange: "))
#Greedy Algorithm
greedy_amount = amount
count = 0

for coin in coins:
    # so if we have 9 coin and the coins list is [1,2,4], it will minus 4 from 9
    # until the number is less than 4
    while greedy_amount >= coin:
        greedy_amount -= coin
        # increment the count number of the coins
        count += 1
print("greedy minimum coins: ", count)

# Dynamic Programming(Optimal solution)

# set the largest number from the amount of the coin provided(it's the amount of
# the coin that need to process)

# because our list starts from 0, so amount in the code will be plus one.
optimal_list = [math.inf]*(amount+1)
# as what I explained above, the first element will be 0
optimal_list[0] = 0
# in python this is typically starts inclusive, for example if I wrote for x in
# range(1, 6), it will be 1,2,3,4,5. 5 times will be run in this loop.
# we could use for y in range(numbers) the numbers/varaible you decide and it
# will run in numbers -1 times and starts from 0
for i in range(1, amount + 1):
    # we don't know the count yet, so we set it to infinite.
    optimal_count = math.inf
    # we want to process the length of the list
    for coin in optimal_coins:
        # so if our i is bigger than the coin we have
        if i >= coin:
            # we want to compare the optimal count from the current one and the
            # optimao count from previous one in the coins list from this
            # optimal list
            optimal_count = min(optimal_count, 1 + optimal_list[i - coin])
    # update the list with newest optimal count
    optimal_list[i] = optimal_count

print("optimal minimum coins: ", optimal_list[amount])

