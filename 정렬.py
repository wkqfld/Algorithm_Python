array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택정렬 : 가장 작은걸 찾아서 가장 앞에 있는 아이와 Swap
"""
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    print("Pass", i, ": ", array)
print("Result :", array)
"""

# 삽입정렬 : 가장 작은걸 찾아서 가장 앞에 위치시키기, 그 뒤는 위치가 +1씩 밀린다
"""
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
    print("Pass", i, ":", array)
        
print("Result :", array)
"""

quickarray = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 퀵정렬 : 배열의 첫 번째 값을 인덱스로 설정하고, 왼쪽에서부터는 인덱스보다 큰 값, 오른쪽에서부터는 인덱스보다 작은 값을 찾은 후 두 값을 스왑한다. 
def quick_sort(array, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
        
        print(array)


    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(quickarray, 0, len(quickarray)-1)
print(quickarray)

"""   
    # 아래는 되는놈
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
            
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
"""  


""" #아래는 안되는놈    
    i = 1
   
    while left <= right:
        while array[left] <= array[pivot] and left <= end:
            left += 1
        while array[right] >= array[pivot] and right > start:
            right -= 1
        
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        
        print("{}번째 array : ".format(i), array)
        i += 1
    
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
"""

