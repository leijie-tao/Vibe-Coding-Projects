from typing import List
from collections import defaultdict
#Hash Table
#defaultdict(list)建立一个默认值为[]的dictionary{}
#首先遍历所有元素，每个元素下再遍历及统计每个字母。以ord()-ord('a')定位index，得到统计每个字母出现次数的list
#list->tuple 作为immutable的key值，具有相同key(相同字母次数)的元素添加至res
#输出结果把dictionary{}转为list[]形式
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            res[key].append(s)
        return list(res.values())



# --- Main 函数用于本地测试 ---

def main():
    print("--- LeetCode #49: 字母异位词分组 本地测试 ---")

    # 实例化 Solution 类
    solution = Solution()

    # 测试用例 1: 基础情况
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = solution.groupAnagrams(strs1)
    print(f"输入: {strs1}")
    # 预期输出 (顺序可能不同): [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print("输出:")
    for group in result1:
        print(f"  {group}")

    print("-" * 30)

    # 测试用例 2: 空字符串和单个字符
    strs2 = ["", "b", ""]
    result2 = solution.groupAnagrams(strs2)
    print(f"输入: {strs2}")
    # 预期输出: [['', ''], ['b']]
    print("输出:")
    for group in result2:
        print(f"  {group}")

    print("-" * 30)

    # 测试用例 3: 只有一种情况
    strs3 = ["a"]
    result3 = solution.groupAnagrams(strs3)
    print(f"输入: {strs3}")
    # 预期输出: [['a']]
    print("输出:")
    for group in result3:
        print(f"  {group}")


# 确保代码只在作为主程序运行时才执行 main() 函数
if __name__ == "__main__":
    main()