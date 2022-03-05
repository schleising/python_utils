import time

class Timer:
    def __init__(self, taskString: str) -> None:
        self.taskString = taskString

    def __enter__(self):
        print(f'{self.taskString}...')
        self.startTime = time.time()

    def __exit__(self, exc_type, exc_value, exc_tb):
        timeElapsed = time.time() - self.startTime
        print(f'{self.taskString} took {timeElapsed:.2f} seconds')

if __name__ == '__main__':
    with Timer('Waiting'):
        time.sleep(2.449)
