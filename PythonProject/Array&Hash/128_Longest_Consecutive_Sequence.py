from typing import List
#hash set
#先找到连续数的首位值(n-1 not in nums)，再判断n+1+1是否存在
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        for n in nums:
            if n-1 in nums:
                continue
            length=1
            while (n + length) in st:
                    length += 1
            res = max(res,length)
        return res


# --- Main 函数用于本地测试 ---

def main():
    print("--- LeetCode #128: 最长连续序列 本地测试 ---")

    # 实例化 Solution 类
    solution = Solution()

    # 测试用例 1: 基础情况
    nums1 = [100, 4, 200, 1, 3, 2]
    # 连续序列是 [1, 2, 3, 4]，长度为 4
    result1 = solution.longestConsecutive(nums1)
    print(f"输入: nums={nums1}")
    print(f"输出: {result1}")  # 预期输出: 4

    # 测试用例 2: 重复数字和无序
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    # 连续序列是 [0, 1, 2, 3, 4, 5, 6, 7, 8]，长度为 9
    result2 = solution.longestConsecutive(nums2)
    print(f"输入: nums={nums2}")
    print(f"输出: {result2}")  # 预期输出: 9

    # 测试用例 3: 空数组
    nums3 = []
    result3 = solution.longestConsecutive(nums3)
    print(f"输入: nums={nums3}")
    print(f"输出: {result3}")  # 预期输出: 0


# 确保代码只在作为主程序运行时才执行 main() 函数
if __name__ == "__main__":
    main()

