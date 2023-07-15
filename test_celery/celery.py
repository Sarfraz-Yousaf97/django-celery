import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_celery.settings')

# Create a new Celery instance.
app = Celery('test_celery')

# Configure Celery using Django settings.
app.config_from_object(settings, namespace='CELERY')

# Discover tasks modules in Django apps.
app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')