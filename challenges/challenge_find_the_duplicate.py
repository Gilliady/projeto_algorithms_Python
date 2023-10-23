def validate_input(nums):
    if not nums or isinstance(nums[0], str) or len(nums) < 2:
        return False
    for num in nums:
        if 0 >= num or not isinstance(num, int):
            return False
    return True


def find_duplicate(nums: list):
    if not validate_input(nums):
        return False
    nums_b = set()
    for num in nums:
        if num in nums_b:
            return num
        nums_b.add(num)
    return False


if __name__ == "__main__":
    find_duplicate([3, 1, 3, 4, 2])
