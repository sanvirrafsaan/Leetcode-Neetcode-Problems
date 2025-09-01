class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotate_num = k % n 
        nums[0:n] = nums[n - rotate_num: n] + nums[0: n - rotate_num]
        return nums
