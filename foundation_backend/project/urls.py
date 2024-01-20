import logging

from django.contrib import admin
from django.urls import path

logger = logging.getLogger(__name__)


def test():
    try:
        10 / 0
    except Exception as e:
        logger.error(e, exc_info=True)


test()

logger.debug("Hello from urls.py")
logger.warning("Hello from urls.py")
logger.error("Hello from urls.py error")

urlpatterns = [
    path("admin/", admin.site.urls),
]
