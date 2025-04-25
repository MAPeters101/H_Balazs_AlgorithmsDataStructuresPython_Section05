# def reverse(nums):
#     # your algorithm here - nums is the list containing the items
#     low_index, high_index = 0, len(nums)-1
#     while low_index < high_index:
#         nums[high_index], nums[low_index] = nums[low_index], nums[high_index]
#         low_index += 1
#         high_index -= 1
#     return nums

def reverse(nums):
    # your algorithm here - nums is the list containing the items
    low_index, high_index = 0, len(nums)-1
    while low_index < high_index:
        nums[high_index], nums[low_index] = nums[low_index], nums[high_index]
        low_index += 1
        high_index -= 1
    return nums

print(reverse([10,20,40,50]))