#i의 부모노드 : (i-1)/2
#i의 자식노드 : 2i+1, 2i+2
def exchange(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    return arr

def percolateDown(arr,targetIndex):
    leftChild=2*targetIndex+1
    rightChild=2*targetIndex+2
    if leftChild>len(arr)-1:
        return arr    
    if arr[targetIndex] < arr[leftChild]:
        arr=exchange(arr,leftChild,targetIndex)
        arr=percolateDown(arr,leftChild)
        arr=percolateDown(arr,rightChild)
    if rightChild>len(arr)-1:
        return arr
    if arr[targetIndex] < arr[rightChild]:
        arr=exchange(arr,rightChild,targetIndex)
        arr=percolateDown(arr,leftChild)
        arr=percolateDown(arr,rightChild)
    return arr


def buildHeap(arr):
    targetIndex=(len(arr)-2)//2  #len(arr)-1의 부모노드부터 시작
    while targetIndex >= 0:
        arr=percolateDown(arr,targetIndex)
        targetIndex-=1

def heapSort(arr):
    result=[]
    while len(arr)>0:
        buildHeap(arr)
        result.append(arr[0])
        arr=arr[1:]
    return result

arr=[3,5,2,5,7,2,1,9]
arr=heapSort(arr)
for i in arr:
    print(i)