from celery import Celery
from time import sleep
from features.stats import Stats


app = Celery('tasks', broker='amqp://localhost', backend='mongodb://localhost:27017/celerytrial')


@app.task(queue="reverse")
def text_reverse(text):
    sleep(25)
    return text[::-1]


@app.task(queue="celery")
def get_stats(text):
    stat = Stats(text)
    char_count = stat.char_count()
    vowel_count = stat.vowel_count()
    return char_count, vowel_count
