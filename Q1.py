def longest_palindromic_substring(s: str) -> str:
    # Get the length of the input string
    n = len(s)
    
    # Create a 2D array to store the results of subproblems
    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome
    dp = [[False for j in range(n)] for i in range(n)]
    
    # Initialize the diagonal elements of dp to True
    # Each character in the input string is a palindrome of length 1
    for i in range(n):
        dp[i][i] = True
    
    # Initialize the longest_palindrome variable to the first character of the input string
    longest_palindrome = s[0]
    
    # Check for palindromes of length 2
    # If two adjacent characters are the same, they form a palindrome of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            longest_palindrome = s[i:i+2]
    
    # Check for palindromes of length 3 and greater
    # For each length l, we check all substrings of length l that start at i
    for l in range(3, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            # A substring s[i:j+1] is a palindrome of length l
            # if the first and last characters are the same and the substring
            # between them (s[i+1:j]) is also a palindrome
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                longest_palindrome = s[i:j+1]
                
    # Return the longest palindromic substring found
    return longest_palindrome

# Get input string from user
s = input("Enter a string: ")

# Call the longest_palindromic_substring function on the input string
result = longest_palindromic_substring(s)

# Output the result
print(f"The longest palindromic substring in '{s}' is '{result}'")
