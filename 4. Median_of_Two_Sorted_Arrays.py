def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        num = sorted(nums1+nums2)
        leng = len(num)
        if leng % 2:
           return num[leng//2]
        elif not leng % 2:
            count = leng//2
            return (num[count-1]+num[count])/2.0

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1,nums2))
        
