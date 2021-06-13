def mergeSort(nums, lenL, lenR):
    print("Original List: ", nums)
    # 1. Divide the list into sublist O(logn)
    if len(nums)==1:
        print("Sorted: ", nums)
        return nums
    elif len(nums)==2:
        a = nums[0]
        b = nums[1]
        if a>b:
            nums = [b,a]
        print("Sorted: ", nums)
        return nums
    else:
        lenL = len(nums)//2
        lenR = len(nums)-lenL
        numsL = nums[:lenL]
        numsR = nums[lenL:]
        print("numsL: ", numsL, ". numsR: ", numsR)
        numsL = mergeSort(numsL, 0, lenL)
        numsR = mergeSort(numsR, 0, lenR)
        result = sortTwoList(numsL,numsR)
        print("Combined: ", result)
        return result

# 2. Combine two sorted list O(n)
def sortTwoList(l1, l2):
    print("I want to sort: ", l1," and ", l2)
    result = []
    sum_len=len(l1)+len(l2)
    while len(result)<sum_len:
        if len(l1)==0:
            result+=l2
        elif len(l2)==0:
            result+=l1
        elif(l1[0]<l2[0]):
            result.append(l1[0])
            l1.pop(0)
        else:
            result.append(l2[0])
            l2.pop(0)
    print("My result is: ", result)
    return result





nums = [10,-2,89,44,2,1,-98]
mergeSort(nums, 0,len(nums)) #O(nlogn)

