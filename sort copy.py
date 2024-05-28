import random

def insertionSort(list):
    key=1
    result=[]
    #전제: result는 정렬된 배열이다
    for num in list:
        #첫번째 항목
        if not result:
            result.append(num)
            continue

        #비교부분
        i=0
        while i<len(result):
            #정렬된 배열값과 비교;
            #result는 정렬된 배열;큰 값을 만나면 삽입
            if result[i]>num:
                j=len(result)-1
                while j>=i:
                    if j==len(result)-1:
                        result.append(result[j])
                    else:
                        result[j+1]=result[j]
                    j-=1
                result[i]=num
                break
            i+=1
            #result 안에 key보다 큰값이 없음;
            if i==len(result):
                result.append(num)
                break

    return result


def mergeSort(list):
    result=[]
    #Base Case
    if len(list)<2:
        return list
    
    #Divide
    mid = len(list)//2
    leftList=list[:mid]
    rightList=list[mid:]

    #Recursive
    leftList=mergeSort(leftList)
    rightList=mergeSort(rightList)

    #Conquer
    i=j=0
    while i<len(leftList) and j<len(rightList):
        if leftList[i]<=rightList[j]:
            result.append(leftList[i])
            i+=1
        else:
            result.append(rightList[j])
            j+=1
    result+=leftList[i:]
    result+=rightList[j:]
    return result

def exchange(list,a,b):
    temp=list[b]
    list[b]=list[a]
    list[a]=temp
    return list

def quickSort(list):
    #Basecase
    if len(list)<=1:
        return list
    if len(list)==2:
        if list[0]<=list[1]:
            return list
        else:
            return exchange(list,0,1)
    
    #Divide
    pivot = list[-1]
    leftList=[]
    rightList=[]
    for i in range(len(list)-1):
        if list[i]>pivot:
            rightList.append(list[i])
        else:
            leftList.append(list[i])
    pivot = [pivot]
    #Conquer
    return quickSort(leftList)+pivot+quickSort(rightList)


        

    

list=[]
for i in range(10):
    list.append(random.randint(0,100))
#print(list)
list=quickSort(list)
#print(list)

