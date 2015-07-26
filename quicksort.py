def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def getMedianPos(A):
    first = A[0]
    last = A[-1]
    if len(A) % 2 == 0:
        mid = A[len(A) // 2 - 1]
    else:
        mid = A[(len(A) - 1) // 2]
    l = [first, mid, last]
    l.sort()
    return A.index(l[1])


def partition(aList, l, r):
    median = getMedianPos(aList[l:r + 1])
    swap(aList, l, median)
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
        global cnt
        cnt = cnt + r - l
        p = partition(aList, l, r)
        quick_sort(aList, l, p - 1)
        quick_sort(aList, p + 1, r)
aList = [3, 7, 1, 2, 4, 5, 6]
cnt = 0
quick_sort(aList, 0, len(aList) - 1)
print cnt
