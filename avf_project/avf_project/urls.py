from django.contrib import admin
from django.urls import path

from avf_handler.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('handler/', index),
]
