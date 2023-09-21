from django.contrib import admin
from .models import Post,BlogPost
# Register your models here.
admin.site.register((Post,BlogPost))