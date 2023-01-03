from django.contrib import admin

# Register your models here.
from dropdownapp.models import Person,Course,Department


admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Person)