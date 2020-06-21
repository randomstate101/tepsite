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
    path('six_hats_selfevaluation/', views.sth_selfevaluation,name='sthselfevaluation'),
	path('six_hats_writeup/',views.six_hats_writeup,name='six_hats_writeup'),
	path('maneffec_selfevaluation/',views.maneffec_selfevaluation,name='maneffec_selfevaluation'),
	path('man_effec_relationship_with_manager/',views.man_effec_relationship_with_manager,name='man_effec_relationship_with_manager'),
	path('man_effec_employee_engagement/',views.man_effec_employee_engagement,name='man_effec_employee_engagement'),
	path('together_win_self_assessment/',views.together_win_self_assessment,name='together_win_self_assessment'),
	path('together_win_peer_review/',views.together_win_peer_review,name='together_win_peer_review'),



]
