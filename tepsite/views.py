from django.shortcuts import render


from django.http import HttpResponse


from .forms import FeedbackForm




def index(request):
	return render(request, 'tepsite/notify.html')
	


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

	