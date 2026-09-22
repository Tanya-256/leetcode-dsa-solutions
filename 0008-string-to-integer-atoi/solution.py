/*
 * Problem: 8. String to Integer (atoi)
 * Link: https://leetcode.com/problems/string-to-integer-atoi/
 * Difficulty: Medium
 * Language: python3
 * Runtime: ✅ 🔥 1 ms Runtime Beats 100% User 🔥 ✅|| Step By Steps Solution ✅ ||  Easy to Understand  ✅🔥 || | Memory: N/A
 */

            i += 1
        elif s[0] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])

            # Handle overflow
            if sign * res > 2**31 - 1:
                return 2**31 - 1
            if sign * res < -2**31:
                return -2**31

            i += 1

        return sign * res

