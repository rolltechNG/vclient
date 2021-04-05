from django.contrib import admin
from datetime import datetime
import base64

from .models import Credential, AccessToken, Unit, VerificationLogs


class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
            [field.name for field in obj._meta.fields] + \
            [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'direction',
                    'access_type', 'units', 'created')
    #search_fields = ['user', 'access_type', 'created']
    list_filter = ('user', 'direction', 'access_type', 'created')


class LogAdmin(ReadOnlyAdmin, admin.ModelAdmin):
    list_display = ('id', 'user', 'input', 'output', 'fuilfiled',
                    'request_type', 'created')
    list_filter = ('user', 'request_type', 'fuilfiled', 'created')


class Credit(Unit):
    readonly_fields = ('direction',)


class AccessTokenAdmin(AccessToken):
    readonly_fields = ('token',)

    def get_readonly_fields(self, request, obj=None):

        return ['token', ]


admin.site.register(Credential)
# admin.site.register(AccessToken)
admin.site.register(AccessToken)
admin.site.register(Unit, UnitAdmin)
admin.site.register(VerificationLogs, LogAdmin)
