import time
from celery import task


@task
def loop_forever():
    count = 0
    while True:
        count += 1
        print "Loop %d" % count
        time.sleep(1)