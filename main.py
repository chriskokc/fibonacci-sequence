# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# recursion approach
# def fib(n):
#     # base case
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# Dynamic programming
# memorisation
# use a map to store the intermediate results of sub-problems
# memo = {0:0, 1:1}
#
#
# def fib(n):
#     # base case
#     if n <= 1:
#         return n
#     # modify the global variable
#     global memo
#     # if the value has not been stored in the map
#     if n not in memo:
#         # we compute and store the value
#         memo[n] = fib(n-1) + fib(n-2)
#     # return the stored value
#     return memo[n]
#
# bottom-up approach
def fib(n):
    # base case
    if n <= 1:
        return n
    # create two variables to keep track of the two previous values
    previous_num = 1
    previous_previous_num = 0
    for i in range(2, n+1):
        # update the two variables
        previous_num += previous_previous_num
        previous_previous_num = previous_num - previous_previous_num
    return previous_num


def print_fib_sequence(n):
    result = ""
    for i in range(n+1):
        result += f", {fib(i)}"
    print(result[2:])