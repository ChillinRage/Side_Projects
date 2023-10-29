# returns first index of the item in the array if found
def LinearSearch(arr, x):
  for i in range(len(arr)):
    if arr[i] == x:
      return i 

  return -1 # not found
