def mean(nums):
    return sum(nums) / len(nums)

def median(nums):
    sorted_numbers = sorted(nums)
    n = len(sorted_numbers)

    if n % 2 == 0:
        mid1 = n // 2
        mid2 = mid1 - 1
        median = (sorted_numbers[mid1] + sorted_numbers[mid2]) / 2
    else:
        median = sorted_numbers[n // 2]

    return median

def mode(nums):
    mode_dict = {}
    for number in nums:
        if number in mode_dict:
            mode_dict[number] += 1
        else:
            mode_dict[number] = 1

    max_count = max(mode_dict.values())
    modes = [number for number, count in mode_dict.items() if count == max_count]

    # Return a single mode if there's only one, otherwise return the first mode in case of multiple
    return modes[0] if len(modes) == 1 else modes[0]
