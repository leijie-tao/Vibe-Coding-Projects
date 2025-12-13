#brute force解法
#外层for遍历用i模拟底部高度，内层for找到i左右两侧的最高位（容器的两端），水位线为左右最高位中的短板即min(leftMax, rightMax)
# 每个i处的水量为水位线- height[i]
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        for i in range(1,len(height)):
            leftmax = rightmax = height[i]
            for j in range(i):
                leftmax = max(leftmax, height[j])
            for j in range(i+1, len(height)):
                rightmax = max(rightmax, height[j])
            result += min(leftmax, rightmax) - height[i]
        return result


#two pointer解法
#优化要点：for loop嵌套依次查找->双指针的移动条件 while l < r:   if
#双指针模式：1️⃣初始化左右指针：
            l, r = 0, len(height)-1
            leftMax, rightMax = height[l], height[r]
            result = 0
#          2️⃣指针移动条件：短板决定水位线，min(leftMax, rightMax)转为指针条件if进入短板内
#          短板内移动指针更新最高位(水位线），并加总指针每个位置的水量result += (最高位-height[l/r])
         while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        return result