# django_app/apps/polls/tasks.py
from celery import shared_task
from common.loggers import logger


@shared_task
def hello_i_am_periodic_task():
    logger.warning("Hello, I am a periodic task!")


@shared_task
def hello_i_am_on_demand_no_priority(a, b, c=100):
    logger.error(f"Hello, I am an on-demand NO PRIORITY task! {(a,b,c)=}")


@shared_task(queue="high_priority")
def hello_i_am_on_demand_high_proirity(x, y, z=200):
    logger.success(f"Hello, I am an on-demand HIGH PRIORITY task! {(x,y,z)=}")


def q():
    hello_i_am_on_demand_no_priority.delay(1, 2)
    hello_i_am_on_demand_no_priority.apply_async(args=[3, 4], queue="default")  # works
    hello_i_am_on_demand_high_proirity.delay(5, 6)
    hello_i_am_on_demand_high_proirity.apply_async(args=[7, 8], queue="default")  # works


# from polls.tasks import hello_i_am_on_demand_no_priority, hello_i_am_on_demand_high_proirity, q
# hello_i_am_on_demand_no_priority.delay(1,2,3) # does not work
# hello_i_am_on_demand_no_priority.apply_async(args=[4, 5, 6], queue='default') # works
# hello_i_am_on_demand_high_proirity.delay(7,8) # works
# hello_i_am_on_demand_high_proirity.apply_async(args=[9,10], queue='default') # works
