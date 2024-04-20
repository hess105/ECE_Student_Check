import msvcrt
import re
import time
import csv

def extract_id(input_string):
    pattern = r'=(\d{10})='  # Regular expression pattern to match 10 digits between '=' signs
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return None

def in_list(arr, low, high, x):
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return True
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return in_list(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return in_list(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

# TEST CASE FOR BINARY SEARCH #
# --------------------------- #
# Test array
#arr = [ 2, 3, 4, 10, 40 ]
#x = 10
 
# Function call
#result = binary_search(arr, 0, len(arr)-1, x)
 
#if result != -1:
#    print("Element is present at index", str(result))
#else:
#    print("Element is not present in array")

### FILE FUNCTIONS ###
# ------------------ #

def csv_update(dow, purdue_id):
 # Generate filename from dow
    filename = f"records/{dow}.csv"
	
	# Init data array
    existing_data = []
	
    # Read data from CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            existing_data.append(row)
    
    # Add the number to each row
    for row in existing_data:
        row.append(purdue_id)
    
    # Write the updated data to the CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(existing_data)
	
    return True

def csv_read(input_string):
    filename = f"records/{input_string}.csv"
    output = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            output.append(row)
    return output

### MERGE SORTING FUNCTIONS ###
# --------------------------- #

# We should only need this during setup.

# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

# This code is contributed by Mohit Kumra

### TEST CASE FOR MERGE SORT ###
#arr = [12, 11, 13, 5, 6, 7]
#n = len(arr)
#print("Given array is")
#for i in range(n):
#    print("%d" % arr[i],end=" ")
# 
#mergeSort(arr, 0, n-1)
#print("\n\nSorted array is")
#for i in range(n):
#    print("%d" % arr[i],end=" ")