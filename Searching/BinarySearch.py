# returns index of item in array if found
# input array must be in sorted order
def BinarySearch(arr, x):
  low, high = 0, len(arr) - 1

  while (low <= high):
    mid = low + (high - low) // 2
    if (arr[mid] == x):
      return mid
      
    if (arr[mid] > x): # search left
      high = mid - 1
    else:
      low = mid + 1
  
  if low == high: return low
  return -1 
