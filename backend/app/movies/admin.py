from django.contrib import admin
from django.utils.translation import gettext as _

from . import models

admin.site.register(models.Movie)
admin.site.register(models.Rating)

