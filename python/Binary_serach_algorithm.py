# -*- coding: utf-8 -*-
"""
Created on Fri Oct  10 13:49:55 2021

@author: DHIRAJ 
"""


# Iterative Binary Search Function
# It returns index of search_value in given list li if present,
# else returns -1
def binary_search(li, Search_value):
	low = 0
	high = len(li) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If search_value is greater, ignore left half
		if li[mid] < Search_value:
			low = mid + 1

		# If search_value is smaller, ignore right half
		elif li[mid] > Search_value:
			high = mid - 1

		# means search_value is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1


# Test list

li = [ 2, 3, 4, 10, 40 ]
Search_value = 4  #you can take value from user as well using int(input()) 

# Function call
result = binary_search(li, Search_value)

if result != -1:
	print("Element is present at index:", str(result))
else:
	print("Element is not present in array")
