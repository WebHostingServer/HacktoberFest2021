def quicksort(nums, start, end):
    if start < end:
        mid = partition(nums, start, end)
        quicksort(nums, start, mid - 1)
        quicksort(nums, mid + 1, end)


def partition(nums, start, end):
    pivot = nums[end]
    i = start - 1
    for j in range(start, end):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    i += 1
    nums[i], nums[end] = nums[end], nums[i]
    return i


if __name__ == "__main__":
    nums = [5, 2, 4, 6, 1, 3]
    quicksort(nums, 0, len(nums) - 1)
    print(nums)
