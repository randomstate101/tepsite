from django.http import Http404


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


from .forms import FeedbackForm

from .models import Program


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
