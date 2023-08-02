from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id' , 'Student_Name' , 'Father_Name' , 'Contact_Number',
                    'Address' , 'Course' , 'Timing' , 'Days' )