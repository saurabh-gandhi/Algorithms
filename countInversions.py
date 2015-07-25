def Count(aList):
    if len(aList) == 1:
        return aList, 0
    else:
        mid = len(aList) // 2
        sorted_left, x = Count(aList[:mid])
        sorted_right, y = Count(aList[mid:])
        sorted_list, z = CountSplitInv(sorted_left, sorted_right)
        return sorted_list, (x + y + z)


def CountSplitInv(left, right):
    items = []
    l, r = 0, 0
    len_left = len(left)
    len_right = len(right)
    splitInversions = 0
    # Merging the left and right list
    for i in range(len_left + len_right):
        lval = left[l] if l < len(left) else None
        rval = right[r] if r < len(right) else None

        if (lval and rval and lval < rval) or rval is None:
            items.append(lval)
            l += 1
        elif (lval and rval and lval >= rval) or lval is None:
            splitInversions += len_left - (l)
            items.append(rval)
            r += 1
        else:
            raise Exception(
                'Could not merge, sub arrays sizes do not match the main array')
    return items, splitInversions
print(Count([1, 3, 5, 2, 4, 6]))
