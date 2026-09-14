# 4. Median of Two Sorted Arrays

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Language: python3](https://img.shields.io/badge/Language-python3-blue?style=for-the-badge)

## Problem Link
[LeetCode - Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Topics
`Array` `Binary Search` `Divide and Conquer`

## Performance Stats
- **Runtime:** Intuitive Python O(log (m+n)) solution, by kth smallest in the two sorted arrays, 252ms
- **Memory:** N/A


## Problem Statement
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


 
Constraints:


	nums1.length == m
	nums2.length == n
	0 <= m <= 1000
	0 <= n <= 1000
	1 <= m + n <= 2000
	-106 <= nums1[i], nums2[i] <= 106

---
*Auto-synced via [SYNTRA - LeetCode to GitHub Tracker](https://github.com/)*
