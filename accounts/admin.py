# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .forms import CoustomUserCreationForm, CoustomUserChangeForm
# from .models import CoustomUser

# class CoustomUserAdmin(UserAdmin):
#     add_form = CoustomUserCreationForm
#     form = CoustomUserChangeForm
#     model = CoustomUser
#     list_display = ['email', 'username', 'age', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + (('Extra Details', {"fields": ("age", "address", "zip", "phone")}),)
#     add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age", "address", "zip", "phone")}),)

# admin.site.register(CoustomUser, CoustomUserAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CoustomUser
from .forms import CoustomUserCreationForm, CoustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    form = CoustomUserChangeForm
    add_form = CoustomUserCreationForm
    model = CoustomUser
    list_display = ('username', 'email', 'age', 'address', 'zip', 'phone')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('age', 'address', 'zip', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'age', 'address', 'zip', 'phone'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CoustomUser, CustomUserAdmin)
