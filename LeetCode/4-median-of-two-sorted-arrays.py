###############################################################################################
# 简单，归并排序
###########
# 时间复杂度：O(n+m)，两个数组长度
# 空间复杂度：O(n+m), 新数组
###############################################################################################
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2, i, j, nums = len(nums1), len(nums2), 0, 0, []
        while i<n1 and j<n2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < n1:
            nums.extend(nums1[i:])
        if j < n2:
            nums.extend(nums2[j:])
        len_ = n1+n2
        if len_%2==0:
            return (nums[len_//2] + nums[len_//2-1])/2
        return nums[len_//2]