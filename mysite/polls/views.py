from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from rest_framework.response import Response

from .forms import CustomUserCreationForm
from .models import Choice, Question, Poll, CustomUser, Votes, Student, Course, Teaches

from django.urls import reverse_lazy
from .auth import AuthBackend
from django.contrib.auth import login, logout
from .forms import StaffLoginForm, StudentLoginForm
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes

import csv

def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:login_staff'))


def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            back = AuthBackend()
            user = back.authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_student:
                    return HttpResponse('Unavailable for students ')
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('polls:personal_page', args=(user.id,)))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = StaffLoginForm()
    return render(request, 'Login/staff_form_login.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            back = AuthBackend()
            user = back.authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                if not user.is_student:
                    return HttpResponse('This is only for students')
                if user.is_active:
                    student = Student.objects.get(email=cd['email'])
                    try:
                        vote = Votes.objects.get(poll=cd['poll_id'], student=student.pk)
                        if vote.voted:
                            return HttpResponse('You have already voted')
                        vote.voted = True
                        vote.save()
                        login(request, user)
                    # todo handle if no such poll exists
                        return HttpResponseRedirect(reverse('polls:detail', args=(cd['poll_id'],)))
                    except Votes.DoesNotExist:
                        return HttpResponse('You should not have access to this poll')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = StudentLoginForm()
    return render(request, 'Login/student_form_login.html', {'form': form})


class PersonalPage(generic.DeleteView):
    model = CustomUser
    template_name = 'home_page/home_page.html'


# for staff self-creation of accounts
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('polls:login_student')
    template_name = 'Login/signup.html'


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published polls."""

        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/default_poll.html'
    # template_name = 'polls/def_poll_tr.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())


def thank_you(request):
    # model = Poll
    template = 'polls/thank_you_page.html'
    context = {}
    return render(request, template, context)


# todo -throw errors is some questions are not answered
def vote_poll(request, poll_id):
   try:
       post_data = dict(request.POST.lists())
       post_data.pop('csrfmiddlewaretoken')
       questions = list(post_data.keys())

       for q in questions:
           quest = get_object_or_404(Question, id=q)
           if quest.type == 2:
               if post_data.get(q)[0] != "":
                    c = Choice.add_choice(question=quest, choice=post_data.get(q)[0]) # counts custom choices with the same text as one choice
                    c.save()
               post_data.pop(q)

       interested = list(post_data.values())
       print(f"Selected choice   {interested}")
   except (KeyError, Choice.DoesNotExist):
       # Redisplay the question voting form.
       return render(request, 'polls/detail.html', {
           # 'question': poll.poll_name,
           'error_message': "You didn't select a choice.",
       })
   else:
       inter = []
       for sublist in interested:
           sublist = [int(item) for item in sublist]
           inter += sublist

       for ch in inter:
           choice = get_object_or_404(Choice, id=ch)
           print(choice.id, "  ", choice.question, "  ", choice.choice_text)
           choice.votes += 1
           choice.save()
       # Always return an HttpResponseRedirect after successfully dealing
       # with POST data. This prevents data from being posted twice if a
       # user hits the Back button.

       return HttpResponseRedirect(reverse('polls:thank_you_page'))


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def course_list(request, prof_id):
    if request.method == 'GET':
        user = CustomUser.objects.get(pk=prof_id)
        if user.is_prof:
            courses_id = set(Teaches.objects.filter(prof=prof_id).values_list('course', flat=True))
            courses = list(Course.objects.filter(id__in=courses_id).values_list('title', flat=True))
        else:
            courses = list(Course.objects.all().values_list('title', flat=True))
    # print({"COURSES": courses})
    return JsonResponse({"COURSES": courses})


def course_list_render(request, prof_id):
    return render(request, 'courses_list/courses_list.html')


def surveys_list_render(request, prof_id):
    return render(request, 'surveys_list/surveys_list.html')


def analytics_render(request, prof_id):
    return render(request, 'analytics/analytics.html')


def calculate_answers(lst, value):
    return sum(list(Choice.objects.filter(question__in=lst).filter(choice_text=value).values_list('votes', flat=True)))


def calculate_avg_grade(lst):
    total_num = 0
    total_sum = 0
    for i in range(1,6):
        s = calculate_answers(lst, str(i))
        total_num += s
        total_sum += s*i
    if total_num > 0:
        return total_sum/total_num
    else:
        return 0


def analytics_help(courses, teaches):
    course_year = list()
    course_grade = list()
    teaches_courses = [t[0] for t in teaches]

    for c in courses:
        indexes = [str(teaches[i][3]) for i, val in enumerate(teaches_courses) if val == c[1]]
        polls = list(Poll.objects.filter(teachers__in=indexes).filter(is_from_default=True).values_list('id'))
        questions = list(Question.objects.filter(poll__in=polls).
                         filter(question_text__in=['Estimate the course - overall',
                                                   'Estimate the course - labs',
                                                   'Estimate the course - lectures & tutorials']).
                         values_list('id'))

        av_grade = calculate_avg_grade(questions)
        course_grade.append({c[0]: str(av_grade)})
        years = set([teaches[i][1] for i, val in enumerate(teaches_courses) if val == c[1]])
        for y in years:
            year_idxs = [i for i, val in enumerate(teaches) if (val[1] == y and val[0] == c[1])]
            year_polls = list(Poll.objects.filter(teachers__in=year_idxs).
                              filter(is_from_default=True).values_list('id'))
            year_questions = list(Question.objects.filter(poll__in=year_polls).
                                  filter(question_text__in=['Estimate the course - overall',
                                                            'Estimate the course - labs',
                                                            'Estimate the course - lectures & tutorials']).
                                  values_list('id'))
            av_grade_y = calculate_avg_grade(year_questions)
            year_grade = {c[0]: str(av_grade_y)}
            course_year.append({y: year_grade})

    return {'COURSE_GRADE': course_grade, 'YEAR_GRADE': course_year}


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def analytics(request, prof_id):
    if request.method == 'GET':
        user = CustomUser.objects.get(pk=prof_id)
        course_year = list()
        course_grade = list()
        if user.is_prof:
            teaches = list(Teaches.objects.filter(prof=prof_id).values_list('course', 'year', 'is_fall', 'id'))
            teachers_id = [i[3] for i in teaches]
            courses = set(Course.objects.filter(teaches__in=teachers_id).values_list('title', 'id'))
            res = analytics_help(courses, teaches)
            return JsonResponse({'PROF': res})
        else:
            courses = set(Course.objects.all().values_list('title', 'id'))
            teaches = list(Teaches.objects.all().values_list('course', 'year', 'is_fall', 'id'))
            res = analytics_help(courses, teaches)
            return JsonResponse({'DOE': res})


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def surveys_list(request, prof_id):
    if request.method == 'GET':
        user = CustomUser.objects.get(pk=prof_id)
        res = list()
        if user.is_prof:
            teaches_query = list(Teaches.objects.filter(prof=prof_id).values_list('id', 'year', 'is_fall'))
            teaches_id = [i[0] for i in teaches_query]
            surveys = list(Poll.objects.filter(teachers__in=teaches_id).
                           values_list('poll_name', 'open_date', 'close_date', 'teachers'))
            for s in surveys:
                teaches_rel = teaches_query[teaches_id.index(s[3])]
                res.append({'poll_title': s[0], 'year': teaches_rel[1], 'semester': teaches_rel[2],
                            'open_date': s[1], 'close_date': s[2]})
        else:
            surveys = list(Poll.objects.values_list('poll_name', 'open_date', 'close_date', 'teachers'))
            for s in surveys:
                teaches_rel = list(Teaches.objects.filter(id=s[3]).values_list('id', 'year', 'is_fall'))[0]
                res.append({'poll_title': s[0], 'year': teaches_rel[1], 'semester': teaches_rel[2],
                            'open_date': s[1], 'close_date': s[2]})
    return JsonResponse({'SURVEYS ': res})


def export_poll(request, poll_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="poll.csv"'
    writer = csv.writer(response)
    for question in Poll.objects.get(pk=poll_id).question_set.all():
        writer.writerow([question.question_text, question.type])
        choices = question.choice_set.all().values_list('choice_text', 'votes')
        for choice in choices:
            writer.writerow(choice)

    return response
