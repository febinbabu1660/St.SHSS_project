from django.contrib import admin
from .models import Account, Sdetails, Course, Subjects,SLanguage, class_Biomaths, class_Commerce, class_HomeScience


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    exclude =('password',)

admin.site.register(Account,UserAdmin)

admin.site.register(Sdetails)

admin.site.register(Course)
admin.site.register(Subjects)
admin.site.register(SLanguage)

admin.site.register(class_Biomaths)
admin.site.register(class_Commerce)
admin.site.register(class_HomeScience)
