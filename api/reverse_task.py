from celery import Celery
from time import sleep
from features.stats import Stats


app = Celery('reverse_task', broker='amqp://localhost', backend='mongodb://localhost:27017/celerytrial')


@app.task(
    queue="reverse",
    max_retries=3
)
def text_reverse(text):
    sleep(25)
    raise Exception("Task Failed.")
    return text[::-1]
