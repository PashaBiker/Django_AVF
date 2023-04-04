from django.contrib import admin
from django.urls import path

from avf_handler.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('handler/', index),
]
