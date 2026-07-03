from utils import StepRecorder

def quick_sort_steps(array):
    length = len(array)
    if length <= 250:
        interval = 1
    else:
        interval = max(1, length // 2)
        
    recorder = StepRecorder(array, step_interval=interval)
    recorder.record(array, [], force=True)
    current  = array.copy()
    
    def partition(arr, start, end):
        pivot = arr[start]
        i = start
        
        for j in range(start + 1, end + 1):
            if arr[j] < pivot:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
                recorder.record(arr,[i, j])
        arr[start], arr[i] = arr[i], arr[start]
        recorder.record(arr, [start, i])
        return i

    def quick_sort(array, start, end):
        if start < end:
            pivot_index = partition(array, start, end)
            quick_sort(array, start , pivot_index -1)
            quick_sort(array, pivot_index + 1, end)
    
    quick_sort(current, 0, len(current) -1)
    
    recorder.record(current, [], force= True)
    
    return recorder.steps