from django.http import Http404


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


from .forms import FeedbackForm

from .models import Program
from .forms import STH_Selfevaluation
from .forms import Six_hats_Writeup
from .forms import Man_eff_SelfEvaluation
from .forms import Man_eff_RelationshipWithManager



#render(request, template_name, context=None, content_type=None, status=None, using=None)¶

def index(request):
	return render(request, 'tepsite/index.html')
@login_required
def manage_effect(request):
    return render(request, 'tepsite/manage_effect.html')
@login_required
def tog_wewin(request):
    return render(request, 'tepsite/tog_wewin.html')
@login_required
def time_man(request):
    return render(request, 'tepsite/time_man.html')
@login_required
def eff_busscom(request):
    return render(request, 'tepsite/eff-busscom.html')
@login_required
def pres_exc(request):
    return render(request, 'tepsite/pres_exc.html')
@login_required
def six_hats(request):
    return render(request, 'tepsite/six_hats.html')
@login_required
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'tepsite/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'tepsite/feedback_form.html', {'tepsite':form})




def responses(request,question_id):
	response = "You are looking at the Responses of Question %s."
	return HttpResponse(response %question_id)



def sth_selfevaluation(request):
    if request.method == 'POST':
        form = STH_Selfevaluation(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'tepsite/thanks.html')
    else:
        form = STH_Selfevaluation()
    return render(request, 'tepsite/six_t_h_selfevaluation.html', {'repsite':form})

def six_hats_writeup(request):
	if request.method == 'POST':
		form = Six_hats_Writeup(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'tepsite/thanks.html')
	else:
		form = Six_hats_Writeup()
	return render(request,'tepsite/six_hats_writeup.html',{'depsite':form})


def maneffec_selfevaluation(request):
	if request.method == 'POST':
		form = Man_eff_SelfEvaluation(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'tepsite/thanks.html')
	else:
		form = Man_eff_SelfEvaluation()
	return render(request, 'tepsite/maneffec_selfevaluation.html',{'sepsite':form})


def man_effec_relationship_with_manager(request):
	if request.method == 'POST':
		form = Man_eff_RelationshipWithManager(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'tepsite/thanks.html')
	else:
		form = Man_eff_RelationshipWithManager()
	return render(request, 'tepsite/man_effec_relationship_with_manager.html',{'aepsite':form})
