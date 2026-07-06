from utils import StepRecorder


def bubble_sort_steps(array):
    
    comparisons = 0
    swaps = 0
    
    # this is the formula for bubble sort only
    length = len(array)
    if length < 100:
        interval = 1
    else:
        interval = max(1, (length**2) // 600)

    recorder = StepRecorder(array, step_interval=interval)

    recorder.record(array, [], force=True)
    length = len(array)
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            comparisons += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swaps += 1
                recorder.record(array, [j, j + 1])
                swapped = True

        if not swapped:
            break
        
    recorder.record(array, [], force=True)

    return recorder.steps, comparisons, swaps
