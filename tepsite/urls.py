from django.conf.urls import url
from django.urls import path


#url(r'^posts/(?P<post_id>[0-9]+)/$', post_detail_view)
#path('posts/<int:post_id>/', post_detail_view)
from . import views

app_name = 'tepsite'



urlpatterns = [

	path('',views.index,name='index'),
	path('managerial_effectiveness/', views.manage_effect, name='managerial_effectiveness'),
	path('together_we_win/', views.tog_wewin, name='together_we_win'),
	path('time_management/', views.time_man, name='time_management'),
	path('business_communication/', views.eff_busscom, name='business_communication'),
	path('presentation_excellence/', views.pres_exc, name='presentation_excellence'),
	path('six_hats/', views.six_hats, name='six_hats'),
    path('feedbackform/', views.feedback_form, name='feedbackform'),



]
