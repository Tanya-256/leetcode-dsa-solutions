/*
 * Problem: 2. Add Two Numbers
 * Link: https://leetcode.com/problems/add-two-numbers/
 * Difficulty: Medium
 * Language: python3
 * Runtime: 1ms 100% ||✅Step By Step Visualization. Easiest to understand. Java, C++, Python, Js | Memory: N/A
 */

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            cur.next = ListNode(total % 10)

        carry = 0
        cur = dummy
        dummy = ListNode()

