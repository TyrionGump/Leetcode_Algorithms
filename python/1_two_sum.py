'''
Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice. 
You can return the answer in any order.
'''

# Brute force: 考虑从头开始计算nums内两两元素的和, 并在计算过程中存储对应两元素的idx. 当找到一个结果时立马返回.
# Comlexity: Time -> O(n^2), Space -> O(n) space暂时分析不出来.....
# Analysis: Runtime: 48ms, Memory: 14.4MB
def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = 0
        for idx_one, i in enumerate(nums):
            idx = [idx_one]
            for idx_two, j in enumerate(nums):
                if idx_one != idx_two:
                    res = i + j
                    if res == target:
                        idx.append(idx_two)
                        return idx

# Dict: 遍历时,不断检查新进入的数字与target之间的差值是否在之前的遍历过程中出现过. 这样就只需要遍历一次.
# Comlexity: Time -> O(n), Space -> O(n)
# Analysis: Runtime: 44ms, Memory: 14.5MB
def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_idx = {}
        
        for idx, i in enumerate(nums):
            cal_res = target - i
            if cal_res in value_to_idx:
                return [value_to_idx[cal_res], idx]
            value_to_idx[i] = idx # 这个地方在判断之后赋值就是为了防止新进入的数字被当成已经遍历过的元素.
