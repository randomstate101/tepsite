from django import forms


from .models import ProgramFeedbackForm
from .models import SixThinkingHats_SelfEvaluation
from .models import Six_hats_Writeup
from .models import Man_eff_SelfEvaluation
from .models import Man_eff_RelationshipWithManager
from .models import Man_eff_Employee_Engagement
from .models import Together_win_Self_Assessment
from .models import Together_win_Peer_Review
from .models import BusinessCommuniction_Self_Assessment


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = ProgramFeedbackForm
        exclude = []
class STH_Selfevaluation(forms.ModelForm):
    class Meta:
        model = SixThinkingHats_SelfEvaluation
        exclude = []

class Six_hats_Writeup(forms.ModelForm):
    class Meta:
        model = Six_hats_Writeup
        exclude=[]

class Man_eff_SelfEvaluation(forms.ModelForm):
    class Meta:
        model = Man_eff_SelfEvaluation
        exclude= []

class Man_eff_RelationshipWithManager(forms.ModelForm):
    class Meta:
        model = Man_eff_RelationshipWithManager
        exclude = []
class Man_eff_Employee_Engagement(forms.ModelForm):
    class Meta:
        model = Man_eff_Employee_Engagement
        exclude=[]
class Together_win_Self_Assessment(forms.ModelForm):
    class Meta:
        model = Together_win_Self_Assessment
        exclude=[]
class Together_win_Peer_Review(forms.ModelForm):
    class Meta:
        model = Together_win_Peer_Review
        exclude=[]
class BusinessCommuniction_Self_Assessment(forms.ModelForm):
    class Meta:
        model = BusinessCommuniction_Self_Assessment
        exclude=[]
