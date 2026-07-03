from utilis import StepRecorder


def merge_sort_steps(array):

    # this formula is only for quick sort and merge sort
    length = len(array)
    if length < 100:
        interval = 1
    else:
        interval = max(1, length // 2)

    recorder = StepRecorder(array, step_interval=interval)

    recorder.record(array, [], force=True)
    current = array.copy()
    start = 0

    def merge_sort(array, start):
        # merge function
        def merge(left, right):
            result = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            return result + left[i:] + right[j:]

        if len(array) <= 1:
            return array
        else:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            left = merge_sort(left, start)
            right = merge_sort(right, start + mid)
            final = merge(left, right)
            current[start : start + len(final)] = final
            recorder.record(current, [i for i in range(start, start + len(final))])
            return final
    
    merge_sort(array, start)
    recorder.record(current, [], force=True)
    return recorder.steps
