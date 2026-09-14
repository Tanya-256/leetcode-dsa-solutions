/*
 * Problem: 4. Median of Two Sorted Arrays
 * Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
 * Difficulty: Medium
 * Language: python3
 * Runtime: Intuitive Python O(log (m+n)) solution, by kth smallest in the two sorted arrays, 252ms | Memory: N/A
 */

        ma = a[ia]
        mb = b[ib]

        if ia + ib < k:
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)

        else:
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

