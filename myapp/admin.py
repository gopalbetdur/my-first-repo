from django.contrib import admin

from .models import TaskList
from .models import RegisteredObject
from .models import TaskObject

admin.site.register(TaskList)
admin.site.register(RegisteredObject)
admin.site.register(TaskObject)

# Register your models here.
