from django import forms


from .models import TestRadioQuestions


CHOICES = [('M','Male'),('F','Female')]
OPTIONS = [("1", "Strongly Disagree"),("2", "Disagree"),("3", "Nuetral"),("4", "Agree"), ("5", "Strongly Agree")]


class TestForm(forms.ModelForm):
    class Meta:
        model = TestRadioQuestions
        exclude = []
	




	
    Gender=forms.ChoiceField(label='Gender',choices=(CHOICES))
    q1 = forms.ChoiceField(label="I think in detail about the problem I am facing",choices=(OPTIONS),widget=forms.RadioSelect())
    q2 = forms.ChoiceField(label="I try to formulate a clear definition of the problem ",choices=(OPTIONS),widget=forms.RadioSelect())
    q4 = forms.ChoiceField(label="I think of the goal and outcome of the problem I am facing",choices=(OPTIONS),widget=forms.RadioSelect())
    q5 = forms.ChoiceField(label="I plan to figure out the most effective method to proceed from the initial problem",choices=(OPTIONS),widget=forms.RadioSelect())
    q6 = forms.ChoiceField(label="I try to organize and arrange my thinking to help move me beyond my present circumstances",choices=(OPTIONS),widget=forms.RadioSelect())
    q7 = forms.ChoiceField(label="I try to figure out what I don't know about the problem",choices=(OPTIONS),widget=forms.RadioSelect())
    q8 = forms.ChoiceField(label="I think of what more I would like to learn from the problem",choices=(OPTIONS),widget=forms.RadioSelect())
    q9 = forms.ChoiceField(label="I think of how I will go about acquiring the facts, stats, and data that will help me resolve this problem",choices=(OPTIONS),widget=forms.RadioSelect())
    q10= forms.ChoiceField(label="I figure out potential solutions exist based on the facts, stats, and data I have collected ",choices=(OPTIONS),widget=forms.RadioSelect())
    q11= forms.ChoiceField(label="I think of what my gut is telling me about a solution",choices=(OPTIONS),widget=forms.RadioSelect())
    q12 = forms.ChoiceField(label="I consider what my feelings tell me about the choice I am about to make",choices=(OPTIONS),widget=forms.RadioSelect())
    q13 = forms.ChoiceField(label="I think of better ways to solve a problem based on my feelings",choices=(OPTIONS),widget=forms.RadioSelect())
    q14 = forms.ChoiceField(label="I think if the solution is the right one based on my intuition",choices=(OPTIONS),widget=forms.RadioSelect())
    q15 = forms.ChoiceField(label="I try to find fatal flaws in a problem",choices=(OPTIONS),widget=forms.RadioSelect())
    q16 = forms.ChoiceField(label="I consider the potential risks and consequences associated with the problem",choices=(OPTIONS),widget=forms.RadioSelect())
    q17 = forms.ChoiceField(label="I think if I have the necessary resources, skills, and support to solve the problem",choices=(OPTIONS),widget=forms.RadioSelect())
    q18 = forms.ChoiceField(label="I think of the best approach to the problem",choices=(OPTIONS),widget=forms.RadioSelect())
    q19 = forms.ChoiceField(label="I think of how I can logically and realistically make the solution work",choices=(OPTIONS),widget=forms.RadioSelect())
    q20 = forms.ChoiceField(label="I think of the positive outcomes that could result from an action",choices=(OPTIONS),widget=forms.RadioSelect())
    q21 = forms.ChoiceField(label="I think of the long-term benefits of an action",choices=(OPTIONS),widget=forms.RadioSelect())
    q22 = forms.ChoiceField(label="I think of the alternative possibilities that could exist when considering a decision",choices=(OPTIONS),widget=forms.RadioSelect())
    q23 = forms.ChoiceField(label="I think of different ways I could approach the problem",choices=(OPTIONS),widget=forms.RadioSelect())
    q24 = forms.ChoiceField(label="I try to think of an out of the box solution",choices=(OPTIONS),widget=forms.RadioSelect())        