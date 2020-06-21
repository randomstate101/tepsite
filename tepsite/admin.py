from django.contrib import admin


from .models import Announcement, Program, Feedback
from .models import ProgramFeedbackForm 



class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('program', 'intern_name', 'date', 'happy',)
	list_filter = ('program', 'date',)
	search_fields = ('program_name', 'details',)

	class Meta:
		model = Feedback





class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('body', 'level', 'display')




admin.site.register(Feedback, FeedbackAdmin)

admin.site.register(Program)

admin.site.register(Announcement)

admin.site.register(ProgramFeedbackForm)
