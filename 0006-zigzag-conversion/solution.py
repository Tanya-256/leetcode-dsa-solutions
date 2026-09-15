/*
 * Problem: 6. Zigzag Conversion
 * Link: https://leetcode.com/problems/zigzag-conversion/
 * Difficulty: Medium
 * Language: python3
 * Runtime: Python O(n) Solution in 96ms (99.43%) | Memory: N/A
 */

                # Move from bottom to top
                while row >= 0 and i < len(s):
                    zigzag[row] += s[i]
                    row -= 1
                    i += 1

                row = 1

            if i >= len(s):
                break

            direction = not direction

        return "".join(zigzag)

