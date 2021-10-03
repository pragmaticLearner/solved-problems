def findMedianSortedArrays(arr1, arr2) -> float:
    new_arr = sorted(arr1 + arr2)
    mid_point = new_arr[len(new_arr) // 2]

    if len(new_arr) % 2 != 0:
        return mid_point
    else:
        return (new_arr[len(new_arr) // 2 - 1] + new_arr[len(new_arr) // 2]) / 2


print(findMedianSortedArrays([12, 3], []))


