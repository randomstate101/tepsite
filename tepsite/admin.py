from django.contrib import admin


from .models import Announcement, Program
from .models import ProgramFeedbackForm
from .models import SixThinkingHats_SelfEvaluation








class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('body', 'level', 'display')






admin.site.register(Program)

admin.site.register(Announcement)

admin.site.register(ProgramFeedbackForm)
admin.site.register (SixThinkingHats_SelfEvaluation)
