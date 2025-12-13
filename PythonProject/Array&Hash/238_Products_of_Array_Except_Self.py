from typing import List
# #Brute force
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         product = 1
#         n = len(nums)
#         result = [0] * n
#         for i in range(n):
#             product=1
#             for j in range(n):
#                 if i == j:
#                     continue
#                 product *= nums[j]
#             result[i] = product
#         return result

#prefix & postfix
#num[0]和nums[n-1]缺少prefix/postfix的值先初始化为1；i在(1,n)上prefix存在，(n-2,-1)上postfix存在
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i +1] * suff[i +1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res



# --- Main 函数用于本地测试 ---

def main():
    print("--- LeetCode #238: 除自身以外数组的乘积 本地测试 ---")

    # 实例化 Solution 类
    solution = Solution()

    # 测试用例 1: 基础情况
    nums1 = [1, 2, 3, 4]
    # 预期输出: [2*3*4, 1*3*4, 1*2*4, 1*2*3] => [24, 12, 8, 6]
    result1 = solution.productExceptSelf(nums1)
    print(f"输入: nums={nums1}")
    print(f"输出: {result1}")

    # 测试用例 2: 包含负数
    nums2 = [-1, 1, 0, -3, 3]
    # 预期输出: [1*0*-3*3, -1*0*-3*3, -1*1*-3*3, -1*1*0*3, -1*1*0*-3] => [0, 0, 9, 0, 0]
    result2 = solution.productExceptSelf(nums2)
    print(f"输入: nums={nums2}")
    print(f"输出: {result2}")

    # 测试用例 3: 单元素数组 (虽然不常见，但也要能处理)
    nums3 = [5]
    # 预期输出: [1]
    result3 = solution.productExceptSelf(nums3)
    print(f"输入: nums={nums3}")
    print(f"输出: {result3}")


# 确保代码只在作为主程序运行时才执行 main() 函数
if __name__ == "__main__":
    main()