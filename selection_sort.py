from utilis import StepRecorder


def selection_sort_steps(array):

    # this is the forumula for selection sort only
    length = len(array)
    if length < 150:
        interval = 1
    else:
        interval = length // 150

    recorder = StepRecorder(array, step_interval=interval)
    recorder.record(array, [], force=True)

    def find_min_index(array, start):
        min_ind = start
        if not array or start >= len(array):
            return min_ind
        for i, value in enumerate(array[start:], start=start):
            if value < array[min_ind]:
                min_ind = i
        return min_ind

    def swap(array, index, swp):
        array[index], array[swp] = array[swp], array[index]
        return array

    for i in range(len(array)):
        min_index = find_min_index(array, i)
        # this condition safes us some useless swaps
        if min_index != i:
            array = swap(array, i, min_index)
            recorder.record(array, [i, min_index])

    recorder.record(array, [], force=True)

    return recorder.steps
