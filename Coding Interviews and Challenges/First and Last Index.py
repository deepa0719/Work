#First Method
def firstLast(arr, target):
    indices = [i for i, x in enumerate(arr) if x == target]
    if len(indices)==0:
        return [-1,-1]
    return [min(indices), max(indices)]
  
#Second Method
def firstLast(arr, target):
    indice = []
    for i in range(len(arr)):
        if arr[i] == target:
            indice.append(i)
    if len(indice)==0:
        return [-1,-1]
    return [min(indice), max(indice)]
