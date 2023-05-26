def find_duplicate(nums):
    if not nums:
        return False
    nums.sort()
    for index in range(len(nums)):
        if (
            index + 1 >= len(nums)
            or not isinstance(nums[index + 1], int)
            or not isinstance(nums[index], int)
            or nums[index] < 0
           ):
            return False
        if nums[index] == nums[index + 1]:
            return nums[index]
    return False

