from typing import List
from collections import Counter, defaultdict
#sorting先统计每个元素的频率，arr按频率顺序由小到大存储(key,value)，res从后向前添加每对键值的[1]位数。
#时间复杂度：构建arr并排序时，对包含M个元素的列表进行排序的复杂度为O(MlogM)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        arr = []
        for num, cnt in d.items():
            arr.append((cnt, num))
            arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

#heap小顶堆推入弹出的复杂度是logK,优化了排序的时间复杂度MlogM
# import heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count=Counter(nums)
#
#         heap = []
#         for element,frequency in count.items():
#             heapq.heappush(heap,(frequency,element))
#             if len(heap) > k:
#                 heapq.heappop(heap)
#
#         result = []
#         for i in heap:
#             result.append(i[1])
#         return result



# --- Main 函数用于本地测试 ---

def main():
    print("--- LeetCode #347: 前 K 个高频元素 本地测试 ---")

    # 实例化 Solution 类
    solution = Solution()

    # 测试用例 1: 基础情况
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = solution.topKFrequent(nums1, k1)
    print(f"输入: nums={nums1}, k={k1}")
    # 预期输出: [1, 2] (顺序可能不同)
    print(f"输出: {result1}")

    # 测试用例 2: 所有元素频率相同
    nums2 = [1]
    k2 = 1
    result2 = solution.topKFrequent(nums2, k2)
    print(f"输入: nums={nums2}, k={k2}")
    print(f"输出: {result2}")  # 预期输出: [1]

    # 测试用例 3: 负数和多重重复
    nums3 = [-1, -1, -2, -2, -2, 3, 3, 3, 3]
    k3 = 2
    result3 = solution.topKFrequent(nums3, k3)
    print(f"输入: nums={nums3}, k={k3}")
    # 频率: {-2: 3, -1: 2, 3: 4}. 预期输出: [3, -2] (顺序可能不同)
    print(f"输出: {result3}")


# 确保代码只在作为主程序运行时才执行 main() 函数
if __name__ == "__main__":
    main()