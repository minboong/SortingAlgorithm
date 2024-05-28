import random
 
def exchange(list,a,b):
    temp=list[b]
    list[b]=list[a]
    list[a]=temp
    return list
 
def percolateDown(arr,targetIndex):
    print("Called")
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
 
list=[]
for i in range(10):
    list.append(random.randint(0,100))
#print(list)
list=heapSort(list)
# for i in list:
#     print(i)