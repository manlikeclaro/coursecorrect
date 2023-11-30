from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from mainapp.models import Product, CustomUser, Category, TeamMember

admin.site.site_header = 'Course Correct'


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_code', 'product_name', 'product_price', 'category', 'sale']


class CustomUserAdmin(admin.ModelAdmin):
    pass
    # list_display = ['user', 'first_name', 'last_name', 'email', 'phone_number', 'dob']
    list_display = ['user', 'phone_number', 'dob', 'profile_picture']


class UsersInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'Accounts'


class CustomizedUserAdmin(UserAdmin):
    inlines = (UsersInline,)
    # fieldsets = UserAdmin.fieldsets + (
    #     ('Custom Fields', {'fields': ('phone_number', 'dob', 'profile_picture')}),
    # )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_tag']


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['member_name', 'member_role', 'profile_picture']


admin.site.register(Product, ProductsAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
