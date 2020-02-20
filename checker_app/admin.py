from django.contrib import admin

from checker_app.models import URL


class URLAdmin(admin.ModelAdmin):
    readonly_fields = ("response_status",)
    fields = ("text", "response_status", "check_interval", "is_paused")


admin.site.register(URL, URLAdmin)
