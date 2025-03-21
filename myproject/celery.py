from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from celery.result import AsyncResult
# from core.tasks import risky_task, task1, task2
from celery import chain, group, shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_url = 'redis://localhost:6379/0'


app.conf.beat_schedule = {
    'daily_summary': {
        'task': 'core.tasks.daily_summary',  
        'schedule': crontab(hour=0, minute=0),  
    },
}


if __name__ == '__main__':
    app.start()
    
app.conf.update(
    broker_url='redis://localhost:6379/0',  
    result_backend='redis://localhost:6379/0',  
)

app.autodiscover_tasks()

# def execute_risky_task():
#     task = risky_task.apply_async(args=[123])  

#     print(f"Task ID: {task.id}") 
#     result = AsyncResult(task.id)
#     print(f"Task Status: {result.status}") 


# task_chain = chain(task1.s(), task2.s())  
# task_chain()

# task_group = group(task1.s(), task2.s())  
# task_group()