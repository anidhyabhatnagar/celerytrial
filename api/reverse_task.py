from celery import Celery
from time import sleep
from features.stats import Stats


app = Celery('reverse_task', broker='amqp://localhost', backend='mongodb://localhost:27017/celerytrial')


@app.task(queue="reverse")
def text_reverse(text):
    sleep(25)
    return text[::-1]
