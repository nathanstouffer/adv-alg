# a short program to mergesort some lists

import random

# method to recursively divide the mergesort
def mergesort(nums):
    mid = int(len(nums) / 2)
    if (mid == 0):
        return nums
    else:
        nums1 = nums[:mid]
        nums2 = nums[mid:]
        return merge(mergesort(nums1), mergesort(nums2))

# method to merge to sorted lists into a single sorted list
def merge(nums1, nums2):
    nums = []
    pos1 = 0
    pos2 = 0
    while (pos1 < len(nums1) or pos2 < len(nums2)):
        if (pos1 >= len(nums1)):
            nums.append(nums2[pos2])
            pos2 += 1
        elif (pos2 >= len(nums2)):
            nums.append(nums1[pos1])
            pos1 += 1
        elif (nums1[pos1] < nums2[pos2]):
            nums.append(nums1[pos1])
            pos1 += 1
        else:
            nums.append(nums2[pos2])
            pos2 += 1
    return nums

nums = []
for i in range(0, 50):
    nums.append(random.randrange(-100, 100))
print("initial:", nums)
nums = mergesort(nums)
print("sorted: ", nums)
