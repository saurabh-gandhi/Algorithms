def merge(left, right):
    items = []
    l, r = 0, 0
    # Merging the left and right list
    for i in range(len(left) + len(right)):
        lval = left[l] if l < len(left) else None
        rval = right[r] if r < len(right) else None

        if (lval and rval and lval < rval) or rval is None:
            items.append(lval)
            l += 1
        elif (lval and rval and lval >= rval) or lval is None:
            items.append(rval)
            r += 1
        else:
            raise Exception(
                'Could not merge, sub arrays sizes do not match the main array')
    return items


def mergeSort(alist):
    if len(alist) == 1:
        return alist
    else:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        sortLeft = mergeSort(left)
        sortRight = mergeSort(right)
        return merge(sortLeft, sortRight)

print(mergeSort([54, 26, 93, 17, 77]))
