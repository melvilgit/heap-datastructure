#!/usr/bin/python
# -*- coding: utf-8 -*-


def max_heapify(arr, i, n):
    if i > 0:
        left = 2 * i
        right = 2 * i + 1
        if left <= n and arr[i - 1] < arr[left - 1]:
            largest = left
        else:
            largest = i

        if right <= n and arr[largest - 1] < arr[right - 1]:
            largest = right
        if arr[largest - 1] > arr[i - 1]:
            (arr[i - 1], arr[largest - 1]) = (arr[largest - 1], arr[i
                    - 1])
        if i != largest:
            max_heapify(arr, largest, n)


def min_heapify(arr, i, n):
    if i > 0:
        left = 2 * i
        right = 2 * i + 1
        if left <= n and arr[i - 1] > arr[left - 1]:
            smallest = left
        else:
            smallest = i

        if right <= n and arr[smallest - 1] > arr[right - 1]:
            smallest = right
        if arr[smallest - 1] < arr[i - 1]:
            (arr[i - 1], arr[smallest - 1]) = (arr[smallest - 1], arr[i
                    - 1])
        if i != smallest:
            min_heapify(arr, smallest, n)

arr=[7,4,6,1,9,8,3,5,2]
i = len(arr) / 2
while i > 0:
    max_heapify(arr, i, 9)
    i -= 1

print arr

			
