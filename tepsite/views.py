from django.http import Http404


from django.shortcuts import render


from django.http import HttpResponse


from .forms import FeedbackForm

from .models import Program


#render(request, template_name, context=None, content_type=None, status=None, using=None)¶

def index(request):
	return render(request, 'tepsite/index.html')

def manage_effect(request):
    return render(request, 'tepsite/manage_effect.html')
    
def tog_wewin(request):
    return render(request, 'tepsite/tog_wewin.html')

def time_man(request):
    return render(request, 'tepsite/time_man.html')    	

def eff_busscom(request):
    return render(request, 'tepsite/eff-busscom.html')

def pres_exc(request):
    return render(request, 'tepsite/pres_exc.html')

def six_hats(request):
    return render(request, 'tepsite/six_hats.html')    

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

	