def migratoryBirds(arr):
  newarr = [0,0,0,0,0,0]
  for bird in range(0, len(arr)):
    newarr[arr[bird]] += 1
  return newarr.index(max(newarr))


arr= [1, 2, 3, 4 ,5, 4 ,3 ,2 ,1, 3, 4]
migratoryBirds(arr)