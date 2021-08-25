from celery import Celery
from time import sleep
from features.stats import Stats


app = Celery('tasks', broker='amqp://localhost', backend='mongodb://localhost:27017/celerytrial')


@app.task(
    bind=True,
    queue="reverse",
    max_retries=2
)
def text_reverse(self, text):
    try:
        sleep(5)
        if text == "Retry Test":
            raise Exception("Failed Task")
    except Exception as e:
        print("Caught Exception: {}. Retrying the task.".format(e))
        self.retry()
    return text[::-1]


@app.task(queue="celery")
def get_stats(text):
    stat = Stats(text)
    char_count = stat.char_count()
    vowel_count = stat.vowel_count()
    return char_count, vowel_count
