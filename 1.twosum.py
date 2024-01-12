def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):              
            if nums[i]+nums[j]==target:
                return [i,j]
        
n = int(input("Listni nechta son bilan to'ldirmoqchisiz: "))
nums = [int(input(f"{i+1}. ")) for i in range(n)]
target = int(input("Son kiriting: "))
print(twoSum(nums,target))