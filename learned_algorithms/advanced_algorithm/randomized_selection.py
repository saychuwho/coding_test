import random


def naive_select(A, k):
    A = sorted(A)
    return A[k]


def partition_about_pivot(A, pivot):
    left, right = [], []
    for num in A:
        if num == pivot: continue
        elif num < pivot:
            left.append(num)
        else:
            right.append(num)
    return left, right


def randomized_select(A, k, c=100):
    if len(A) <= c:
        return naive_select(A, k)
    pivot = random.choice(A)
    left, right = partition_about_pivot(A, pivot)
    if len(left) == k:
        return pivot
    elif len(left) > k:
        return randomized_select(left, k, c)
    else:
        return randomized_select(right, k-len(left) - 1, c)