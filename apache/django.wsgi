import os
import sys

path = '/usr/local/django-apps/'
if path not in sys.path:
        sys.path.append(path)
path = '/usr/local/django-apps/zachtib_com'
if path not in sys.path:
        sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'zachtib_com.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

