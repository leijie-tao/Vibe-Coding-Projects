class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}
        for i,num in enumerate(nums):
            indices[num]=i
        for i,num in enumerate(nums):
            diff=target-num
            if diff in indices and indices[diff]!=i:
                return [i,indices[diff]]


def main():
    # 实例化 Solution 类
    solver = Solution()

    # --- 测试用例 1 ---
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solver.twoSum(nums1, target1)
    print(f"输入: nums={nums1}, target={target1}")
    print(f"结果: {result1}")  # 期望输出: [0, 1]

    # --- 测试用例 2 ---
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solver.twoSum(nums2, target2)
    print(f"\n输入: nums={nums2}, target={target2}")
    print(f"结果: {result2}")  # 期望输出: [1, 2]

    # --- 测试用例 3 ---
    nums3 = [3, 3]
    target3 = 6
    result3 = solver.twoSum(nums3, target3)
    print(f"\n输入: nums={nums3}, target={target3}")
    print(f"结果: {result3}")  # 期望输出: [0, 1]


if __name__ == "__main__":
    main()