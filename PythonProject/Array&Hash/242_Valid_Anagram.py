from typing import List
#利用内置sorted()，返回排序后的string比较是否得到同样的结果
#sort()仅用于list且原地修改原列表，sorted()可用于任何可迭代对象且不修改原对象
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

#hash map统计每个字母出现的次数，s记+1，t记-1，看最后所有元素是否全部抵消。
# from collections import defaultdict
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         dic=defaultdict(int)
#         if len(s)!=len(t):
#             return False
#         for i in s:
#             dic[i]+=1
#         for i in t:
#             dic[i]-=1
#         for i in dic:
#             if dic[i]!=0:
#                 return False
#         return True




# --- Main 函数用于本地测试 ---

def main():
    print("--- LeetCode #242: 有效的字母异位词 本地测试 ---")

    # 实例化 Solution 类
    solution = Solution()

    # 测试用例 1: 有效的异位词
    s1, t1 = "anagram", "nagaram"
    result1 = solution.isAnagram(s1, t1)
    print(f"输入: s='{s1}', t='{t1}'")
    print(f"输出: {result1}")  # 预期输出: True

    # 测试用例 2: 无效的异位词 (长度相同，内容不同)
    s2, t2 = "rat", "car"
    result2 = solution.isAnagram(s2, t2)
    print(f"输入: s='{s2}', t='{t2}'")
    print(f"输出: {result2}")  # 预期输出: False

    # 测试用例 3: 长度不同 (在第一步被排除)
    s3, t3 = "a", "ab"
    result3 = solution.isAnagram(s3, t3)
    print(f"输入: s='{s3}', t='{t3}'")
    print(f"输出: {result3}")  # 预期输出: False


# 确保代码只在作为主程序运行时才执行 main() 函数
if __name__ == "__main__":
    main()