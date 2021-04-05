from django.contrib import admin
from datetime import datetime
import base64

from .models import Credential, AccessToken, Unit


class AccessTokenAdmin(AccessToken):
    readonly_fields = ('token',)

    def get_readonly_fields(self, request, obj=None):

        return ['token', ]


admin.site.register(Credential)
# admin.site.register(AccessToken)
admin.site.register(AccessToken)
admin.site.register(Unit)
