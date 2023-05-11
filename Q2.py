def max_coins(piles):
    # Get the length of the input list of piles
    n = len(piles)
    
    # If there are only 1 or 2 piles, we can just pick all the coins
    if n <= 2:
        return sum(piles)
    
    # Create a 1D array to store the maximum number of coins that can be picked
    # from the first i piles without picking from adjacent piles
    dp = [0] * n
    
    # Initialize the first two elements of dp to the values of the first two piles
    dp[0] = piles[0]
    dp[1] = piles[1]
    
    # Iterate over the remaining piles and calculate the maximum number of coins
    # that can be picked without picking from adjacent piles
    for i in range(2, n):
        # We have two choices:
        # 1. Pick the current pile and the pile two piles ago (dp[i-2] + piles[i])
        # 2. Don't pick the current pile (dp[i-1])
        dp[i] = max(dp[i-2] + piles[i], dp[i-1])
        
    # The maximum number of coins that can be picked without picking from adjacent piles
    # is stored in the last element of dp
    return dp[-1]

# Get input list of piles from user
piles = input("Enter a list of piles (comma-separated): ")

# Convert input string to list of integers
piles = [int(p) for p in piles.split(',')]

# Call the max_coins function on the input list of piles
result = max_coins(piles)

# Output the result
print(f"The maximum number of coins that can be picked without picking from adjacent piles is {result}")
