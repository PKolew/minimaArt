from django.contrib.auth.models import Group, Permission, User
from django.contrib import admin
from .models import CustomerProfile

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')

def initialize_roles():

    if not Group.objects.filter(name="Superuser").exists():
        Group.objects.create(name="Superuser")

    if not Group.objects.filter(name="Staff").exists():
        staff_group = Group.objects.create(name="Staff")

        permissions = Permission.objects.filter(codename__in=["add_product", "change_product"])
        staff_group.permissions.set(permissions)

initialize_roles()
