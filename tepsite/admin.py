from django.contrib import admin


from .models import Announcement, Program
from .models import ProgramFeedbackForm
from .models import SixThinkingHats_SelfEvaluation
from .models import Six_hats_Writeup
from .models import Man_eff_SelfEvaluation
from .models import Man_eff_RelationshipWithManager
from .models import Man_eff_Employee_Engagement
from .models import Together_win_Self_Assessment
from .models import Together_win_Peer_Review
from .models import BusinessCommuniction_Self_Assessment
from .models import Presentation_Self_Assessment








class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('body', 'level', 'display')






admin.site.register(Program)

admin.site.register(Announcement)

admin.site.register(ProgramFeedbackForm)
admin.site.register (SixThinkingHats_SelfEvaluation)
admin.site.register(Six_hats_Writeup)
admin.site.register(Man_eff_SelfEvaluation)
admin.site.register(Man_eff_RelationshipWithManager)
admin.site.register(Man_eff_Employee_Engagement)
admin.site.register(Together_win_Self_Assessment)
admin.site.register(Together_win_Peer_Review)
admin.site.register(BusinessCommuniction_Self_Assessment)
admin.site.register(Presentation_Self_Assessment)
admin.site.site_header = 'JSW Steel administration'
