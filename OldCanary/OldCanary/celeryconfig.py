# -*- coding: UTF-8 -*-
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OldCanary.settings")

from django.conf import settings

celery_app = Celery(
    "OldCanary", backend="rpc://", broker="amqp://guest:guest@rabbitmq:5672//"
)
celery_app.config_from_object(settings)
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
