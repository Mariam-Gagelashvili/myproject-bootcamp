import logging
from celery import shared_task, chain, group
import random
from django.core.mail import send_mail
import time

@shared_task
def send_welcome_email(user_id):
    print(f'email sent for {user_id}')
    

@shared_task
def daily_summary():
    logging.info("Daily summary task executed.")
    print("Daily summary task is running")
    
    
@shared_task
def send_email_task(user_email):
    time.sleep(5)  
    return f"Email sent to {user_email}"

@shared_task
def periodic_task():
    print("This runs every 10 seconds")


@shared_task(bind=True, max_retries=3)
def risky_task(self, some_id):
    try:
        print(f"Processing {some_id}...")  
        if random.choice([True, False]):  
            raise ValueError("Random failure occurred!")
        print(f"Task {some_id} completed successfully!")
    except Exception as exc:
        print(f"Task failed! Retrying in 10 seconds...")
        raise self.retry(exc=exc, countdown=10) 
    
    
# @shared_task
# def task1():
#     print("Task 1 completed!")
#     return "Result from task1"

# @shared_task
# def task2(result_from_task1):
#     print(f"Task 2 received: {result_from_task1}")
#     return "Result from task2"

# def execute_tasks():
#     task_chain = chain(task1.s(), task2.s())
#     task_chain.apply_async()  

#     task_group = group(task1.s(), task2.s())
#     task_group.apply_async()


# @shared_task
# def send_welcome_email(user_email):
#     send_mail(
#         subject="Welcome to Our Platform!",
#         message="Thanks for signing up. We’re glad to have you!",
#         from_email="admin@example.com",
#         recipient_list=[user_email],
#         fail_silently=False,
#     )
#     return f"Email sent to {user_email}"