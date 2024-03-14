def merge(L, R):
    result = []
    l_idx, r_idx = (0,0)

    while l_idx < len(L) and r_idx < len(R):
        if L[l_idx] < R[r_idx]:
            result.append(L[l_idx])
            l_idx += 1
        else:
            result.append(R[r_idx])
            r_idx += 1
    
    result.extend(L[l_idx:len(L)])
    result.extend(R[r_idx:len(R)])

    return result


def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    left = merge_sort(A[0:n//2])
    right = merge_sort(A[n//2:n])
    return merge(left, right)


A = [5, 4, 7, 3, 9, 2]
print(merge_sort(A))