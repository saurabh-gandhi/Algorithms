def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(aList, l, r):
    p = aList[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if aList[j] < p:
            swap(aList, i, j)
            i = i + 1
    swap(aList, l, i - 1)
    return i - 1


def quick_sort(aList, l, r):
    if l < r:
        p = partition(aList, l, r)
        quick_sort(aList, l, p - 1)
        quick_sort(aList, p + 1, r)
aList = [54, 26, 93, 17, 77]
quick_sort(aList, 0, 4)
print aList
