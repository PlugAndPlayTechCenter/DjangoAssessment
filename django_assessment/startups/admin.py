from django.contrib import admin

# Register your models here.
from django_assessment.startups.models import Startup,Stage,Country,Contact,Prescriptor

admin.site.register(Stage)
admin.site.register(Country)
admin.site.register(Contact)
admin.site.register(Prescriptor)
admin.site.register(Startup)