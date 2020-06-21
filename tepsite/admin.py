from django.contrib import admin


from .models import Announcement, Program
from .models import ProgramFeedbackForm
from .models import SixThinkingHats_SelfEvaluation
from .models import Six_hats_Writeup
from .models import Man_eff_SelfEvaluation
from .models import Man_eff_RelationshipWithManager








class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('body', 'level', 'display')






admin.site.register(Program)

admin.site.register(Announcement)

admin.site.register(ProgramFeedbackForm)
admin.site.register (SixThinkingHats_SelfEvaluation)
admin.site.register(Six_hats_Writeup)
admin.site.register(Man_eff_SelfEvaluation)
admin.site.register(Man_eff_RelationshipWithManager)
