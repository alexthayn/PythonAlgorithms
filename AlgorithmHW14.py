# Return the length of the longest palindromic subsequence given a sequence x[1...n]
def longestPalindrome(x):
    n = len(x)
    lengths = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        lengths[i][i] = 1
    
    for s in range(2,n+1):
        for i in range(n-s+1):
            j = i + s - 1
            if x[i] == x[j] and s == 2: 
                lengths[i][j] = 2
            elif x[i] == x[j]:
                lengths[i][j] = lengths[i+1][j-1] + 2
            else:
                lengths[i][j] = max(lengths[i][j-1], lengths[i+1][j])
    return lengths[0][n-1]
    
if __name__ == "__main__":
    sequence = "acgtctcaaaatcg"

    print(longestPalindrome(sequence))