from django import forms


from .models import ProgramFeedbackForm


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = ProgramFeedbackForm
        exclude = []
