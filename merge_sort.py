from utils import StepRecorder


def merge_sort_steps(array):

    # this formula is only for quick sort and merge sort
    length = len(array)
    if length <= 250:
        interval = 1
    else:
        interval = max(1, length // 2)

    recorder = StepRecorder(array, step_interval=interval)

    recorder.record(array, [], force=True)
    current = array.copy()
    comparisons = 0
    swaps = 0
    
        
    def merge(arr, start, mid, end):
        nonlocal comparisons, swaps
        i = start
        j = mid + 1
        temp = []
        while i <= mid and j <= end:
            comparisons += 1
            if arr[j] < arr[i]:
                temp.append(arr[j])
                j += 1
            else:
                temp.append(arr[i])
                i += 1
                
        while i <= mid:
            temp.append(arr[i])
            i += 1
            
        while j <= end:
            temp.append(arr[j])
            j += 1
            
        
        for k in range(start, end + 1):
            arr[k] = temp[k - start]
            swaps += 1
            recorder.record(arr, [k])
                
    def merge_sort(arr, start, end):
        if start < end:
            mid = (start + end) // 2
            merge_sort(arr, start, mid)
            merge_sort(arr, mid + 1, end)
            merge(arr, start, mid, end)
            
    merge_sort(current, 0, len(current)- 1)   
     
    recorder.record(current, [], force=True)
    
    return recorder.steps, comparisons, swaps