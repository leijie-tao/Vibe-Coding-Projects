#brute force
#两次遍历，搜索所有符合条件的结果
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

#hash map
#优化要点：利用哈希表查询时间复杂度O(1)的特点，用一次遍历搭建map，节约第二次遍历时间
#思路：利用enumerate同时调用index，value，一边遍历并存储以value为key的map，一边查询target-n是否在map中
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, n in enumerate(nums):
            if (target - n) in mp:
                return [mp[target - n], i]
            mp[n] = i





# --- Main 函数用于本地测试 ---

def main():
    print("--- LeetCode #1: Two Sum 本地测试 ---")

    # 实例化 Solution 类
    solution = Solution()

    # 测试用例 1: 基础情况
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"输入: nums={nums1}, target={target1}")
    print(f"输出: {result1}")  # 预期输出: [0, 1] 或 [1, 0]

    # 测试用例 2: 负数和重复数字
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"输入: nums={nums2}, target={target2}")
    print(f"输出: {result2}")  # 预期输出: [1, 2] 或 [2, 1]

    # 测试用例 3: 没有解的情况
    nums3 = [1, 5, 9, 13]
    target3 = 10
    result3 = solution.twoSum(nums3, target3)
    print(f"输入: nums={nums3}, target={target3}")
    print(f"输出: {result3}")  # 预期输出: []


# 确保代码只在作为主程序运行时才执行 main() 函数
if __name__ == "__main__":
    main()