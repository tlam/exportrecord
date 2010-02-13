from django.contrib import admin
from django.contrib.admin.models import LogEntry
 
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user_no_link', 'action_time', 'object_repr', 'change_message')
    search_fields = ('user__username',)

    def user_no_link(self, obj):
        return u'</a>%s<a>' % obj.user
    user_no_link.allow_tags = True
    user_no_link.short_description = 'user'

admin.site.register(LogEntry, LogEntryAdmin)
