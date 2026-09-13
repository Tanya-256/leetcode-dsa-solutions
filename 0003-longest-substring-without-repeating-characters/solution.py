/*
 * Problem: 3. Longest Substring Without Repeating Characters
 * Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * Difficulty: Medium
 * Language: python3
 * Runtime: N/A | Memory: N/A
 */


            for j in range(i, len(s)):
                ch = s[j]

                if ch not in temp:
                    temp += ch
                else:
                    break
        for i in range(len(s)):
            temp = ""

    def lengthOfLongestSubstring(self, s):
        max_len = 0
class Solution:

