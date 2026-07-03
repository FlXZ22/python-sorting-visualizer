class StepRecorder:
    def __init__(self, arr, step_interval=1):
        length = len(arr)
        self.steps = []
        self.step_count = 0
        self.step_interval = step_interval
    def record(self, arr, highlight_indices, force=False):
        self.step_count += 1
        if force or self.step_count % self.step_interval == 0:
            step = {"array": arr.copy(), "highlight_indices": highlight_indices.copy()}
            self.steps.append(step)
