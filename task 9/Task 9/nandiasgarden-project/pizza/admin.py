from django.contrib import admin

from .models import Pizza, Size, Intern, Task

admin.site.register(Pizza)
admin.site.register(Size)

admin.site.register(Intern)
admin.site.register(Task)