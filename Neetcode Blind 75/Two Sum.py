link to problem: https://neetcode.io/problems/is-anagram?list=blind75
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [4, 5, 6], target = 10
        #iter 1: i=0, val = 4. diff = 6. add 4:0 to valmap {4:0}
        #iter 2: i=1, val=5. diff = 5. Action: add 5:1 to valmap {4:0, 5:1}
        #iter 3: i=2, val = 6. diff = 4. 4 in valmap and 2 != 0. return it. 
        val_map = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in val_map and i != val_map[diff]:
                return [val_map[diff], i]
            else:
                val_map[val] = i
