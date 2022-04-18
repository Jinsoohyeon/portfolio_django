from django.contrib import admin
from .models import Memo, Mail

# Register your models here.

admin.site.register(Memo)

admin.site.register(Mail)