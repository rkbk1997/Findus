from django.contrib import admin
from findusapp.models import *
from adminapp.models import *
from userapp.models import *
# Register your models here.
admin.site.register(Registration)
admin.site.register(Cate)
admin.site.register(Subcate)
admin.site.register(Feedback)
admin.site.register(Location)
admin.site.register(Payment)
