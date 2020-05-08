from django.urls import path
from django.conf.urls import url


from . import views

app_name = 'polls'

urlpatterns = [
# ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    url('thank_you_page/', views.thank_you, name='thank_you_page'),
    path('<int:poll_id>/vote/', views.vote_poll, name='vote'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^login_staff/$', views.staff_login, name='login_staff'),
    url(r'^login_student/$', views.student_login, name='login_student'),
    path('<int:pk>/user', views.PersonalPage.as_view(), name='personal_page'),

    url(r'(?P<prof_id>[0-9]+)/courses_api/$', views.course_list, name='course_list'),
    url(r'(?P<prof_id>[0-9]+)/courses/$', views.course_list_render, name='course_list_render'),
    # url(r'(?P<prof_id>[0-9]+)/courses/$', views.surveys_list, name='surveys_list'),

]

