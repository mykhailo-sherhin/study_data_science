import schedule
import time


def task():
    print('Hello! I am a task!')
    return


schedule.every(10).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)