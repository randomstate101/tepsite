from django import forms


from .models import ProgramFeedbackForm
from .models import SixThinkingHats_SelfEvaluation


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = ProgramFeedbackForm
        exclude = []
class STH_Selfevaluation(forms.ModelForm):
    class Meta:
        model = SixThinkingHats_SelfEvaluation
        exclude = []
