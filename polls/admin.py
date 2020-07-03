from django.contrib import admin

from .models import Question

admin.site.register(Question)  # Question obj have an admin interface

