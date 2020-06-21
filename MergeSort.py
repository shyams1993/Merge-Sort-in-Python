arr = [5,6,2,4,1,3,8,7]

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    mid = length // 2
    left = arr[:mid]
    print(left)
    right = arr[mid:]
    print(right)
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    result = []
    leftptr = 0
    rightptr = 0
    while leftptr < len(left) and rightptr < len(right):
        if left[leftptr] < right[rightptr]:
            result.append(left[leftptr])
            leftptr+=1
        elif right[rightptr] < left[leftptr]:
            result.append(right[rightptr])
            rightptr+=1
    return result + left[leftptr:] + right[rightptr:]

print(mergeSort(arr))
