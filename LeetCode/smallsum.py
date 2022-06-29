def small_sum(arr: list, low, high):
    if low == high:
        return 0
    mid = low + ((high - low) >> 1)
    return small_sum(arr, low, mid) + small_sum(arr, mid + 1, high) + merge(arr, low, mid, high)


def merge(arr: list, low, mid, high):
    temp = [-1] * len(arr)
    i, j, k, ans = low, mid + 1, low, 0
    while i <= mid and j <= high:
        if arr[i] > arr[j]:
            ans += high - j + 1
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= high:
        temp[k] = arr[j]
        k += 1
        j += 1
    for i in range(low, high + 1):
        arr[i] = temp[i]
    return ans


if __name__ == '__main__':
    arr = [7, 5, 6, 4]
    print(small_sum(arr, 0, len(arr) - 1))
    print(arr)
