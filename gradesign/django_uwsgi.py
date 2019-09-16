import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gradesign.settings")

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()    版本升级之后此处会报错  详情看最后
from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()