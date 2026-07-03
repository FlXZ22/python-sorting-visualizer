from utilis import StepRecorder


def quick_sort_steps(array):

    # this formula is only for quick sort and merge sort
    length = len(array)
    if length < 100:
        interval = 1
    else:
        interval = max(1, length // 2)

    recorder = StepRecorder(array, step_interval=interval)
    recorder.record(array, [], force=True)
    current = array.copy()

    def quick_sort(arr, start):
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]

        sorted_left = quick_sort(left, start)
        sorted_right = quick_sort(right, start + len(sorted_left) + 1)

        result = sorted_left + [pivot] + sorted_right
        current[start : start + len(result)] = result
        recorder.record(current, [i for i in range(start, start + len(result))])
        return result

    quick_sort(current, 0)
    recorder.record(current, [], force=True)
    return recorder.steps
