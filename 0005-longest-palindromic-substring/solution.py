/*
 * Problem: 5. Longest Palindromic Substring
 * Link: https://leetcode.com/problems/longest-palindromic-substring/
 * Difficulty: Medium
 * Language: python3
 * Runtime: N/A | Memory: N/A
 */

        for i in range(n):
            dp[i][i] = True

        ans = s[0]

        for j in range(n):
            for i in range(j):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j == i + 1):
                    dp[i][j] = True

                    if j - i + 1 > len(ans):
                        ans = s[i:j + 1]

        return ans      

