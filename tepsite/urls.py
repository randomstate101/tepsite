from django.conf.urls import url
from django.urls import path


#url(r'^posts/(?P<post_id>[0-9]+)/$', post_detail_view)
#path('posts/<int:post_id>/', post_detail_view)
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:question_id>/', views.details, name='details'),
	path('<int:question_id>/responses', views.responses, name='responses'),

]