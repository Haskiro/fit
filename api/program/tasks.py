from celery import shared_task
from program.models import Program


@shared_task
def count_programs():
    count = Program.objects.count()

    return count