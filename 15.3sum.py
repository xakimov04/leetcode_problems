def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                summ = nums[i]+nums[left]+nums[right]
                if summ < 0:
                    left += 1
                elif summ > 0:
                    right -= 1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return result
    
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))