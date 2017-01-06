#!/usr/bin/python
# -*- coding: utf-8 -*-


def max_heapify(arr, i, n):
        left = 2 * i +1
        right = 2 * i + 2
        if left <= n and arr[i] < arr[left]:
            largest = left
        else:
            largest = i

        if right <= n and arr[largest] < arr[right]:
            largest = right
        if arr[largest] > arr[i]:
            (arr[i], arr[largest]) = (arr[largest], arr[i])
        if i != largest:
            max_heapify(arr, largest, n)


def min_heapify(arr, i, n):
        left = 2 * i+1
        right = 2 * i + 2
        if left <= n and arr[i] > arr[left]:
            smallest = left
        else:
            smallest = i

        if right <= n and arr[smallest] > arr[right]:
            smallest = right
        if arr[smallest] < arr[i]:
            (arr[i], arr[smallest]) = (arr[smallest], arr[i])
        if i != smallest:
            min_heapify(arr, smallest, n)

arr=[7,4,6,1,9,8,3,5,2]
i = len(arr) / 2
while i >= 0:
    min_heapify(arr, i, 8)
    i -= 1

print arr

			
