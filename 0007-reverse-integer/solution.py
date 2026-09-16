/*
 * Problem: 7. Reverse Integer
 * Link: https://leetcode.com/problems/reverse-integer/
 * Difficulty: Medium
 * Language: python3
 * Runtime: ✅ My C++Solution Beats 100% || 0ms Run time ✅ | Memory: N/A
 */

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0

