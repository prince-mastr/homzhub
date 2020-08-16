from django.contrib import admin
from .models import State,Request_type,Request, Status

admin.site.register(State)
admin.site.register(Request_type)
admin.site.register(Request)
admin.site.register(Status)