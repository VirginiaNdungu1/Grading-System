from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from . models import Profile, Program, Module, Unit, Days, Assessment, Project

#
# class UnitAdmin(admin.ModelAdmin):
#     filter_horizontal = ('sharing_modules', 'lec',)


class DayAdmin(admin.ModelAdmin):
    filter_horizontal = ('unit_days',)


class ModuleAdmin(admin.ModelAdmin):
    filter_horizontal = ('enrolled_students', 'common_units',)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    filter_horizontal = ('modules', 'programs', 'units')


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'is_active', 'get_role', 'get_program_code', 'get_module_code', 'get_phone_number', 'get_reg_date')
    list_select_related = ('profile',)

    def get_acceptance_code(self, instance):
        return instance.profile.acceptance_code
    get_acceptance_code.short_description = 'Acceptance Code'

    def get_role(self, instance):
        return instance.profile.roles
    get_role.short_description = 'ROLE'

    def get_module_code(self, instance):
        for module in instance.profile.modules.all():
            return module.code
    get_module_code.short_description = 'Module'

    def get_program_code(self, instance):
        for program in instance.profile.programs.all():
            return program.code
    get_program_code.short_description = 'Program'

    def get_id_number(self, instance):
        return instance.profile.id_number
    get_id_number.short_description = 'National ID'

    def get_phone_number(self, instance):
        return instance.profile.phone_number
    get_phone_number.short_description = 'Phone Number'

    def get_reg_date(self, instance):
        return instance.profile.reg_date
    get_reg_date.short_description = 'Reg Date'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# Register your models here.

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Program)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Unit, DayAdmin)
admin.site.register(Days)
admin.site.register(Assessment)
admin.site.register(Project)
