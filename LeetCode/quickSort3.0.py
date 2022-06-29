import random


def quick_sort(arr, l, r):
    if l < r:
        low, high = partation(arr, l, r)
        quick_sort(arr, l, low - 1)
        quick_sort(arr, high + 1, r)


def partation(arr, l, r):
    i, low, high = l, l - 1, r
    n = random.randint(l, r)
    arr[n], arr[r] = arr[r], arr[n]
    while i < high:
        if arr[i] < arr[r]:
            low += 1
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
        elif arr[i] > arr[r]:
            high -= 1
            arr[i], arr[high] = arr[high], arr[i]
        else:
            i += 1
    arr[r], arr[high] = arr[high], arr[r]
    return low + 1, high


def check_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                return False
    else:
        return True


if __name__ == '__main__':
    arr = [random.randint(1, 100) for x in range(random.randint(10, 100))]
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
    print(check_sort(arr))
