from typing import List
#brute force
#两次遍历每个数，寻找是否存在重复值
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False


#hash set
#利用hash set的去重功能
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st=set(nums)
        if len(st) != len(nums):
            return True
        else:
            return False



# --- Main 函数用于本地测试 ---

def main():
    print("--- LeetCode #217: 存在重复元素 本地测试 ---")

    # 实例化 Solution 类
    solution = Solution()

    # 测试用例 1: 存在重复
    nums1 = [1, 2, 3, 1]
    result1 = solution.hasDuplicate(nums1)
    print(f"输入: nums={nums1}")
    print(f"输出: {result1}")  # 预期输出: True

    # 测试用例 2: 不存在重复
    nums2 = [1, 2, 3, 4]
    result2 = solution.hasDuplicate(nums2)
    print(f"输入: nums={nums2}")
    print(f"输出: {result2}")  # 预期输出: False

    # 测试用例 3: 复杂重复情况
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result3 = solution.hasDuplicate(nums3)
    print(f"输入: nums={nums3}")
    print(f"输出: {result3}")  # 预期输出: True

    # 测试用例 4: 空数组
    nums4 = []
    result4 = solution.hasDuplicate(nums4)
    print(f"输入: nums={nums4}")
    print(f"输出: {result4}")  # 预期输出: False


# 确保代码只在作为主程序运行时才执行 main() 函数
if __name__ == "__main__":
    main()