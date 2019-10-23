# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.




class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        current = m+n-1
        m -= 1
        n -= 1
        while len(nums2) > 0:
            if m < 0 or nums1[m] <= nums2[n]:
                nums1[current] = nums2.pop(n)
                n -= 1
            else:
                nums1[current] = nums1[m]
                m -= 1

            current -= 1
        return nums1
