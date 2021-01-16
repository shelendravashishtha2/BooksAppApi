from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Branch)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Payment)