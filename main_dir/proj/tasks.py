import time

from celery import shared_task


@shared_task
def test_task():
    print('task running')
    time.sleep(5)
