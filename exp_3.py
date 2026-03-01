import pandas as pd

def med_table(s1, s2):

    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first column
    for i in range(m + 1):
        dp[i][0] = i

    # Initialize first row
    for j in range(n + 1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # Deletion
                dp[i][j - 1] + 1,      # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )

    # Create DataFrame
    df = pd.DataFrame(dp, index=[''] + list(s1), columns=[''] + list(s2))

    print(df)

med_table("cat", "hat")

# part 2

def med(s1, s2):

    m, n = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first column
    for i in range(m + 1):
        dp[i][0] = i

    # Initialize first row
    for j in range(n + 1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,        # Deletion
                dp[i][j - 1] + 1,        # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )

    # Print the table
    print("  ", end="")
    for j in range(n + 1):
        if j == 0:
            print("  ", end="")
        else:
            print(s2[j - 1] + " ", end="")
    print()

    for i in range(m + 1):
        if i == 0:
            print("  ", end="")
        else:
            print(s1[i - 1] + " ", end="")

        for j in range(n + 1):
            print(dp[i][j], end=" ")
        print()

    return dp[m][n]


# Test the function

print("Example 1: Typo (substitution)")
print("MED:", med("kitten", "sitten"))

print("\nExample 2: Insertion")
print("MED:", med("cat", "chat"))

print("\nExample 3: Deletion")
print("MED:", med("chat", "cat"))

print("\nExample 4: Multiple operations")
print("MED:", med("abcdef", "azced"))
